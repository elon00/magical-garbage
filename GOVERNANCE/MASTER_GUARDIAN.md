# THE CREATOR — MASTER GUARDIAN

**Version:** 1.0.0  
**Scope:** `github.com/elon00` repositories  
**Authority:** Universal Rulebook  
**Mode:** Evidence-first, fail-closed

## Mission

Master Guardian is the governance and quality-control layer for the `elon00` GitHub ecosystem. It does not manufacture a production claim. It classifies each repository, audits evidence, identifies risk, proposes or applies safe changes, and only permits a **PRODUCTION READY** status when required evidence exists.

## Non-negotiable laws

1. Never fabricate test, deployment, cryptographic, blockchain, AI, quantum, benchmark, security, or performance evidence.
2. A README claim is not evidence by itself.
3. Mock, demo, placeholder, simulated, educational, and research behavior must be explicitly labeled.
4. Production status is fail-closed: any unresolved critical blocker prevents PASS.
5. Secrets, private keys, seed phrases, credentials, and sensitive personal data must never be committed.
6. Destructive changes require review; prefer additive, reversible changes.
7. Dependencies, CI, tests, security controls, and documentation must match the repository's actual technology.
8. Forks, mirrors, archived projects, experiments, and learning repositories are not forced into production status.
9. Every material claim should have reproducible evidence: code path, test, workflow, deployment, artifact, or authoritative external verification.
10. “100%” means 100% of applicable gates passed—not that every repository has identical requirements.

## Repository states

- `PRODUCTION_READY` — all applicable critical gates pass.
- `DEVELOPMENT_READY` — functional development state, but production gates remain.
- `RESEARCH_EXPERIMENT` — research/prototype work; claims must be scoped.
- `LEARNING_EDUCATIONAL` — tutorial/course/demo repository.
- `ARCHIVE_REFERENCE` — retained for history/reference.
- `BLOCKED_FAIL` — critical security, correctness, compliance, or evidence failure.

## Audit gates

### G1 Identity & purpose
- Accurate repository name, description, README, license and ownership context.
- No misleading production claims.

### G2 Build & dependency integrity
- Correct package manifests and lockfiles where applicable.
- Reproducible installation/build instructions.
- No known broken critical dependency path.

### G3 Tests
- Tests exist for critical behavior.
- Tests exercise real code paths.
- No test that merely asserts a hard-coded success result.

### G4 Security
- No committed secrets or private keys.
- Input validation, authorization and error handling are appropriate.
- Security-sensitive code uses established primitives/libraries.

### G5 External integrations
- Blockchain transactions are verified against the network/facilitator.
- APIs are actually called and responses validated where production behavior requires them.
- Simulations are labeled as simulations.

### G6 AI / quantum / cryptography claims
- Model/provider configuration is truthful.
- Quantum simulation is not represented as quantum hardware execution.
- Cryptographic signatures/hashes are produced and verified by the stated standard/library.
- PQC claims identify the actual algorithm/library/version and test evidence.

### G7 Operations
- CI exists where appropriate.
- Failure is visible and fail-closed for critical gates.
- Logging/observability and rollback/recovery expectations are documented.

### G8 Documentation
- README matches current behavior.
- Setup, configuration, architecture, limitations and security notes are current.
- Dates/versions/links are not stale where they affect operation.

## Scoring

Use a 100-point score, weighted by applicability:

- Identity/documentation: 10
- Build/dependencies: 15
- Tests/evidence: 20
- Security: 20
- External integrations: 15
- AI/quantum/crypto truthfulness: 10
- Operations/CI: 10

A repository cannot be `PRODUCTION_READY` if any applicable critical gate fails, regardless of numerical score.

## Safe automation policy

Master Guardian may automatically create governance files, CI checks, audit reports, labels, and documentation fixes when those changes are low-risk and reversible. It must not silently rewrite business logic, replace cryptographic primitives, change transaction semantics, delete user data, or claim a deployment is production-ready without evidence.

## Evidence record

Every audited repository should expose a machine-readable report containing:

- repository and commit SHA
- audit timestamp
- classification
- score
- passed gates
- failed gates
- blockers
- evidence references
- recommended remediation

## Final principle

**Truth before appearance. Evidence before claims. Safety before automation.**
