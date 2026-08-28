#!/usr/bin/env python3
"""Deterministic, dependency-free evidence guard for THE CREATOR Master Guardian."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'.git', 'node_modules', '.venv', 'venv', '__pycache__'}
TEXT_EXT = {'.md', '.txt', '.json', '.yml', '.yaml', '.toml', '.js', '.mjs', '.ts', '.tsx', '.jsx', '.py', '.rs', '.go', '.java', '.sol', '.sh'}

CLAIMS = [
    r'100%\s*(secure|production|ready)',
    r'production[- ]ready',
    r'quantum\s+hardware',
    r'post[- ]quantum\s+secure',
    r'verified\s+on[- ]chain',
    r'fully\s+autonomous',
]
SIMULATION_MARKERS = re.compile(r'\b(mock|mocked|simulation|simulated|placeholder|demo|stub|fake)\b', re.I)


def files():
    for p in ROOT.rglob('*'):
        if not p.is_file() or any(part in EXCLUDED for part in p.parts):
            continue
        if p.suffix.lower() in TEXT_EXT or p.name in {'Dockerfile', 'Makefile'}:
            yield p


def main():
    findings = []
    claim_hits = []
    simulation_hits = []
    for p in files():
        try:
            text = p.read_text(encoding='utf-8', errors='strict')
        except (UnicodeDecodeError, OSError):
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            for pattern in CLAIMS:
                if re.search(pattern, line, re.I):
                    claim_hits.append((p.relative_to(ROOT), line_no, line.strip()))
            if SIMULATION_MARKERS.search(line):
                simulation_hits.append((p.relative_to(ROOT), line_no, line.strip()))

    if not (ROOT / 'GOVERNANCE' / 'repository-policy.yml').exists():
        findings.append('Missing GOVERNANCE/repository-policy.yml')
    if not (ROOT / 'GOVERNANCE' / 'MASTER_GUARDIAN.md').exists():
        findings.append('Missing GOVERNANCE/MASTER_GUARDIAN.md')

    print('MASTER GUARDIAN EVIDENCE GUARD')
    print('Repository:', ROOT.name)
    print('Claim findings:', len(claim_hits))
    print('Simulation/placeholder markers:', len(simulation_hits))

    if findings:
        for item in findings:
            print('BLOCKER:', item)
        return 1

    # Claims and simulation markers are informational in the control-plane repository;
    # they are never converted into positive evidence automatically.
    print('Result: GOVERNANCE CHECK PASSED')
    print('Note: This is not a production-readiness certification.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
