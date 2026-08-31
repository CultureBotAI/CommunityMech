# Deep-research providers

This Mech supports two first-class deep-research lanes:

- `openscientist` through `deep-research-client`;
- `codex` through the native `codex exec` contract in
  `scripts/deep_research_contract.py`.

Codex is intentionally not routed through the client's `cyberian` adapter.
The native command explicitly enables web search, runs ephemerally in a
read-only sandbox, requires a JSON-schema response, validates report length and
distinct HTTP(S) sources, and publishes atomically only after validation.

## Credentials

Codex uses the local Codex CLI login. Run `codex login status`; no API key is
stored in this repository.

OpenScientist requires:

```bash
export OPENSCIENTIST_API_KEY='name:secret'
# Optional; this is the default:
export OPENSCIENTIST_URL='https://www.openscientist.io'
```

The `name:secret` shape is required by the fleet contract. Never commit either
value or print it in logs.

## Canary sequence

Run the non-billing checks first:

```bash
just deep-research-canary codex
just deep-research-canary openscientist
```

The Codex canary verifies CLI authentication and support for native web search,
output schema, and last-message capture. The OpenScientist canary validates the
credential shape and confirms that `deep-research-client providers` discovers
the provider. It does not submit a hosted job.

Before any batch or paid run, execute one real target, inspect the report and
its cited sources, and only then authorize a bounded batch. Research artifacts
are curator inputs; they never update records automatically.

## Canonical pin

`scripts/deep_research_contract.py` is vendored byte-for-byte from the
canonical `CultureBotAI/culturebotai-claw` artifact. Fleet-governed Mechs pin
it through `scripts/.vendored_canon_ref`; repositories outside that manifest
use `scripts/.deep_research_contract_ref`. Do not let local copies evolve
independently.
