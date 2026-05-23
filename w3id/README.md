# w3id.org redirect for CommunityMech

This directory stages the upstream pull request to
[perma-id/w3id.org](https://github.com/perma-id/w3id.org) that registers
`https://w3id.org/communitymech/` as a permanent identifier prefix for
CommunityMech CURIEs.

## Files

- `communitymech/.htaccess` — redirect rules. Copy verbatim to
  `communitymech/.htaccess` in a fork of `perma-id/w3id.org` and open a PR.

## Resolution targets

| URL                                                          | Target                                                                                    |
|--------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| `https://w3id.org/communitymech/`                            | `https://culturebotai.github.io/CommunityMech/`                                           |
| `https://w3id.org/communitymech/<Name>`                      | `https://culturebotai.github.io/CommunityMech/communities/<Name>.html`                    |
| `https://w3id.org/communitymech/<Name>.html`                 | same as above                                                                             |
| `https://w3id.org/communitymech/<Name>.yaml`                 | `https://raw.githubusercontent.com/CultureBotAI/CommunityMech/main/kb/communities/<Name>.yaml` |
| `https://w3id.org/communitymech/schema/communitymech.yaml`   | `https://raw.githubusercontent.com/CultureBotAI/CommunityMech/main/src/communitymech/schema/communitymech.yaml` |

`<Name>` is the community filename slug (e.g., `EcoFAB_Ring_Trial_SynCom17`)
that matches `kb/communities/<Name>.yaml`. CommunityMech also assigns each
record a numeric identifier (`CommunityMech:NNNNNN`) which is recorded in
the YAML body but not used as the URL path component.

## Schema prefix update

The LinkML schema's `communitymech` prefix was shortened from
`https://w3id.org/culturebot-ai/communitymech/` to
`https://w3id.org/communitymech/` in the same change that added this
directory, so that the registered redirect matches the schema.

## Submission

1. Fork `perma-id/w3id.org`.
2. Copy `communitymech/` from this directory into the fork root.
3. Open a PR following the contribution guidelines in that repo
   (`CONTRIBUTING.md`). Use this directory's README as PR context.

Issue: [CultureBotAI/CommunityMech#12](https://github.com/CultureBotAI/CommunityMech/issues/12)
