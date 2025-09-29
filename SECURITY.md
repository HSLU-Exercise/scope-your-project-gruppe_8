# Security Policy

## Policy Enforcement Script
Dieses Repository verwendet ein eigenes Python-Skript (`scripts/policy_enforcer.py`),
das bei jedem Pull Request automatisch läuft. Es prüft Code auf:
- Hardcodierte Passwörter
- Verwendung von `eval()`
- Debug-Ausgaben

Wenn Verstöße gefunden werden, schlägt der Pull Request fehl.

## Sicherheitslücken melden
Falls du eine echte Sicherheitslücke in diesem Projekt entdeckst,
bitte **nicht öffentlich posten**, sondern per E-Mail an mich@example.com melden.
