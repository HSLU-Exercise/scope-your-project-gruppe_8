# Security Policy

# Sicherheitsrichtlinien für dieses Projekt

Dieses Projekt benutzt eine automatische **Security-Policy-Prüfung** (policy_enforcer.py).
Damit wollen wir verhindern, dass unsichere Dinge in den Code kommen.

## 🚫 Was wir nicht im Code wollen

### 1. Hardcodierte Passwörter
> **Was ist das?**  
> Ein Passwort direkt in den Code schreiben.
>
> **Warum ist das schlecht?**  
> Das ist so, als würdest du deinen Haustürschlüssel an die Tür malen.  
> Jeder, der den Code sieht, kann dein Passwort sehen.
>
> **Was machen wir stattdessen?**  
> Passwörter werden z. B. aus einer sicheren Datei oder aus Umgebungsvariablen geholt,
> nicht direkt im Code gespeichert.

---

### 2. Verwendung von `eval()`
> **Was ist das?**  
> `eval()` führt Text aus, als wäre es Programmcode.
>
> **Warum ist das schlecht?**  
> Stell dir vor, du hast einen Zauberkasten, in den jeder Fremde etwas reinlegen darf.  
> Er könnte damit alles Mögliche anstellen und dein Programm kaputt machen oder Daten klauen.
>
> **Was machen wir stattdessen?**  
> Wir benutzen feste Funktionen oder sichere Parser statt `eval()`.

---

### 3. Debug-Ausgaben
> **Was ist das?**  
> Zusätzliche `print("DEBUG…")` Ausgaben, die beim Entwickeln helfen.
>
> **Warum ist das schlecht?**  
> Das ist wie Notizzettel beim Lego-Bauen. Im fertigen Modell willst du keine Zettel sehen,
> weil sie oft interne Informationen verraten.
>
> **Was machen wir stattdessen?**  
> Debug-Ausgaben entfernen oder durch ein Logging-System ersetzen,
> das im Live-Betrieb ausgeschaltet werden kann.

---

## ✅ Automatische Prüfung
Jeder Pull Request wird automatisch von `scripts/policy_enforcer.py` geprüft.
Wenn einer dieser Punkte verletzt wird, stoppt GitHub den Pull Request,
bis es behoben ist.

