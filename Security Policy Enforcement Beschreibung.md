# Security Policy Enforcement — minimal demo

Dieses Repo demonstriert **Security Policy Enforcement**:
- Lokaler pre-commit Hook blockiert Commits mit unsicheren Patterns.
- GitHub Actions PR-Check blockiert Merge, wenn Policies verletzt werden.

## Warum?
- Sicherheitsrichtlinien (Policies) helfen, Fehler & Schwachstellen früh zu erkennen.
- Ohne Enforcement verlassen sich Teams nur auf Reviews → menschliche Fehler möglich.
- Automatisierte Checks garantieren einheitliche Code-Qualität & Sicherheit.

## Demo-Policies
- Keine Hardcoded-Passwörter (`password = "..."`).
- Kein `eval()` im Code.
- Kein `print("DEBUG")` in Produktivcode.

## Dateien im Repo
- `scripts/policy_enforcer.py` — Policy-Checker Script.
- `.git/hooks/pre-commit` — Beispiel-Hook lokal.
- `.github/workflows/policy-enforce.yml` — GitHub Actions Workflow.
- `insecure_demo.py` — Datei mit absichtlichen Policy-Verstößen.

## Demo (lokal)
1. Mach den Hook ausführbar:
   ```bash
   chmod +x .git/hooks/pre-commit
