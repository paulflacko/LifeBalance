# 07 · Erinnerungen

Erinnerungen sind freiwillig, einzeln schaltbar und standardmäßig sparsam. Die Hantelwoche nutzt dafür **ntfy** (kostenlose App, kein Konto, auch auf der Apple Watch). LifeBalance übernimmt das Verfahren. Anleitung für Nutzer: [archiv-hantelwoche/09-benachrichtigungen-anleitung.md](archiv-hantelwoche/09-benachrichtigungen-anleitung.md).

## Arten

| Erinnerung | Standard | Wann | Säule |
|---|---|---|---|
| Morgen-Check-in | an | 07:00, entfällt, wenn schon ausgefüllt | Erholung |
| Krafttraining | an | 30 min vor dem Block, mit Übungen, Entlastungswoche, Ampel | Körper |
| Bewegung und Mobility | an | 10 min vor Spaziergang, Mobility, Yoga, Ausdauer, Zirkel | Körper |
| Meditation am Abend | an | 22:00, mit Magnesium-Hinweis | Geist |
| Sonntag: Meal Prep und Wochenrückblick | an | 16:00 und 19:00 | Ernährung, Wachstum |
| Supplements | aus | zu den Zeiten aus dem Plan, nur was noch offen ist | Ernährung |
| Skill-Impuls | aus | Di, Do, Sa 17:00, wechselt zwischen den angehefteten Zielen | Wachstum |
| Schlafenszeit | aus | 22:30 | Erholung |
| *Neu:* Abendrückblick | aus | 20:30 | Geist |
| *Neu:* eigene Tracker | aus | frei wählbar (z. B. Wasser 11:00 und 15:00) | je Tracker |

In LifeBalance kann jedes Modul Erinnerungen anmelden; die Liste oben sind die mitgelieferten.

## Regeln

- **Erledigt = keine Erinnerung.** Wer etwas abhakt, löscht die schon eingeplante Nachricht.
- Die App plant bei jedem Öffnen die nächsten 2 Tage ein (einstellbar 1–3; ntfy.sh erlaubt höchstens 3 Tage Vorlauf). Wer die App länger nicht öffnet, bekommt danach keine Erinnerungen mehr.
- Tippen auf eine Erinnerung öffnet die passende Stelle der App ([Deep-Links](02-navigation.md#deep-links)).
- Der Kanalname ist zufällig und geheim. „Neuen Kanal erzeugen“ ersetzt ihn.
- Ausschalten löscht alle eingeplanten Nachrichten.

## Technik

- Senden als JSON an `https://ntfy.sh/` ohne eigene Header (keine CORS-Vorabfrage), Feld `delay` = Unix-Zeit, `sequence_id` = `lb-JJJJMMTT-<art>`.
- Erneutes Senden mit gleicher Kennung ersetzt die eingeplante Nachricht; `GET /<kanal>/<kennung>/delete` löscht sie.
- Einstellungen und Kanal liegen nur auf dem Gerät.
