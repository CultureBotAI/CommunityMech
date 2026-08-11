"""Standard helper for appending CurationEvent entries to a MicrobialCommunity.

Every script that mutates a community YAML should call
``record_curation_event`` to leave an audit trail. Centralizing here means:

* timestamps are ISO-8601 with UTC tz, consistently;
* the ``curation_history`` slot is created on demand;
* re-runs of idempotent migration scripts can short-circuit when the most
  recent event already matches (``skip_if_recent`` flag);
* the schema's ``CurationEvent`` field names (timestamp / curator / action /
  changes / llm_assisted) are honored, so future schema diffs only need to
  touch one file.

Drop-in usage::

    from communitymech.curate.curation_event import record_curation_event

    record_curation_event(
        community,
        curator="add_community_ids",
        action="ASSIGN_COMMUNITY_ID",
        changes=f"Assigned id={community['id']}",
    )

Ported from the sibling helpers in CultureMech, MediaIngredientMech, and
TraitMech. The CommunityMech ``CurationEvent`` schema does not define
``notes``, ``source``, ``previous_status``, ``new_status``, or
``llm_model`` — those keyword arguments are intentionally absent here.
Pass narrative detail in ``changes``.
"""

from __future__ import annotations

import datetime
import re
from typing import Any

import yaml

__all__ = ["record_curation_event", "append_curation_event_text", "now_iso"]


def now_iso() -> str:
    """Current UTC timestamp matching the repo's existing convention.

    Whole-second precision with a ``Z`` suffix
    (e.g. ``"2026-05-25T05:30:12Z"``). Matches the format used by the
    sibling Mech repos so cross-repo tooling can read curation events
    uniformly.
    """
    iso = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    return iso.replace("+00:00", "Z")


def record_curation_event(
    doc: dict[str, Any],
    *,
    curator: str,
    action: str,
    changes: str | None = None,
    llm_assisted: bool = False,
    timestamp: str | None = None,
    skip_if_recent: bool = False,
) -> dict[str, Any]:
    """Append a CurationEvent to ``doc['curation_history']``.

    Args:
        doc: The MicrobialCommunity dict being mutated. Mutated in place.
        curator: Script / human identifier (e.g. ``"add_community_ids"``
            or ``"jane.smith"``). Required because the schema requires it.
        action: SCREAMING_SNAKE_CASE action label (e.g.
            ``"ASSIGN_COMMUNITY_ID"``, ``"FIX_NETWORK_INTEGRITY"``).
            Required; must match the schema's pattern
            ``^[A-Z][A-Z0-9]*(_[A-Z0-9]+)*$``.
        changes: Optional human-readable description of what changed.
            Maps to ``CurationEvent.changes``.
        llm_assisted: True when an LLM produced this change. When True
            the field is emitted; when False the field is omitted so
            downstream consumers can distinguish "explicitly not LLM"
            from "older event written before this field existed".
        timestamp: Override the ISO-8601 timestamp (used for tests /
            deterministic snapshots). Defaults to current UTC.
        skip_if_recent: When True, do nothing if the most recent
            ``curation_history`` entry already matches the same
            ``(curator, action)`` pair. Useful when refactoring a script
            into the helper without producing duplicate trail entries
            during a re-run.

    Returns:
        The appended event dict (or the most recent matching one if
        ``skip_if_recent`` short-circuited).
    """
    history = doc.setdefault("curation_history", [])
    if history is None:
        doc["curation_history"] = history = []

    if skip_if_recent and history:
        last = history[-1]
        if (
            isinstance(last, dict)
            and last.get("curator") == curator
            and last.get("action") == action
        ):
            return last

    event: dict[str, Any] = {
        "timestamp": timestamp or now_iso(),
        "curator": curator,
        "action": action,
    }
    if changes is not None:
        event["changes"] = changes
    if llm_assisted:
        event["llm_assisted"] = True

    history.append(event)
    return event


def append_curation_event_text(
    text: str,
    *,
    curator: str,
    action: str,
    changes: str,
    width: int = 100,
    timestamp: str | None = None,
) -> str:
    """Append one CurationEvent to a record's `curation_history`, as text.

    Text rather than a YAML round-trip because every write path here is a
    line-level editor: re-dumping the document would reformat all of it, and
    `_assert_only_grounding_changed` exists precisely because four hand-rolled
    attempts at whole-file edits corrupted records (#378).

    Two cases. When `curation_history` is absent — 310 of the 312 records, since
    #325 is still open — the key is appended at the end of the document. When it
    is present, the event goes at the end of its block, found by scanning to the
    next top-level key. Appending a second `curation_history:` instead would be
    silently lossy, since PyYAML keeps only the last of two identical keys; the
    duplicate-key detector in the write guard would catch it, but producing it
    and relying on the guard is the wrong order.
    """
    # Built by the shared helper rather than by hand: it owns the field names
    # and the timestamp format, and `audit_writers.py` cannot tell a hand-rolled
    # dict from the real thing — its check is a regex for the literal
    # `'curator':`, so a drifting copy would keep reporting `yes` (review of
    # #483). Only the *insertion* has to be bespoke here, because every write
    # path in this module is a line-level editor.
    holder: dict = {}
    record_curation_event(
        holder, curator=curator, action=action, changes=changes, timestamp=timestamp
    )
    event = holder["curation_history"][0]
    dumped = yaml.dump(
        [event], sort_keys=False, allow_unicode=True, width=width, default_flow_style=False
    ).rstrip("\n")

    lines = text.rstrip("\n").split("\n")
    # A document end marker would put the appended key outside the document.
    if any(ln.rstrip() in ("...", "---") for ln in lines[1:]):
        raise ValueError(
            "record uses explicit YAML document markers; curation_history cannot "
            "be appended safely by line edit (#395)."
        )
    for i, line in enumerate(lines):
        # `curation_history:`, `curation_history: []`, `curation_history:  # note`
        # are the same key. Matching the bare string alone appended a SECOND
        # `curation_history:` for the other two, which PyYAML resolves by
        # keeping only the last — silently dropping the existing history. The
        # write guard caught it, but producing corruption and relying on the
        # guard is the wrong order (review of #483).
        head = re.match(r"^curation_history:\s*(.*)$", line)
        if not head:
            continue
        rest = head.group(1).strip()
        if rest and not rest.startswith("#"):
            # An inline value: `curation_history: []`. Replace it with a block,
            # since an event cannot be appended to a flow sequence by line edit.
            if rest not in ("[]", "~", "null"):
                raise ValueError(
                    f"record has an inline curation_history value ({rest!r}) that "
                    f"is not an empty list; refusing to edit it (#395)."
                )
            lines[i] = "curation_history:"
        end = len(lines)
        for j in range(i + 1, len(lines)):
            # Only a new top-level KEY ends the block. `- timestamp: ...` also
            # starts at column 0 — testing `not line[0].isspace()` treated the
            # list's own first item as the next section and inserted the event
            # ABOVE the existing history, which the append-only write guard then
            # correctly refused. Match the same `^[A-Za-z_]` rule the rest of
            # this module uses to find section ends.
            if re.match(r"^[A-Za-z_]", lines[j]):
                end = j
                break
        # Back off over a comment block introducing that next key, so the event
        # is not inserted below it — which would silently re-attach the comment
        # to curation_history.
        while end > i + 1 and lines[end - 1].lstrip().startswith("#"):
            end -= 1
        while end > i + 1 and not lines[end - 1].strip():
            end -= 1
        # An indented sequence (`  - action: ...`) cannot take a column-0 item.
        items = [ln for ln in lines[i + 1 : end] if ln.strip().startswith("- ")]
        indent = " " * (len(items[0]) - len(items[0].lstrip())) if items else ""
        body = [f"{indent}{ln}" if ln.strip() else ln for ln in dumped.split("\n")]
        return "\n".join(lines[:end] + body + lines[end:]) + "\n"
    return "\n".join(lines + ["curation_history:"] + dumped.split("\n")) + "\n"
