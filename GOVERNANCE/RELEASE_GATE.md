# THE CREATOR Release Gate

A production release is allowed only when the repository's audit record contains:

- [ ] Correct project classification
- [ ] Reproducible build evidence
- [ ] Reproducible test evidence
- [ ] Security/secret-hygiene evidence
- [ ] Dependency review evidence where applicable
- [ ] External integration evidence where applicable
- [ ] Accurate production/research/simulation documentation
- [ ] Commit SHA and implementation references
- [ ] No unresolved critical blockers

## Fail-closed rule

If any applicable critical gate is unknown, missing, or failing, the release status is **BLOCKED**. Do not convert an unknown state into PASS.

## Special handling

Cryptographic, blockchain/payment, financial, authentication, authorization, and destructive changes require explicit review. Research or simulated functionality may ship as research/simulation only when clearly labelled and isolated from production claims.
