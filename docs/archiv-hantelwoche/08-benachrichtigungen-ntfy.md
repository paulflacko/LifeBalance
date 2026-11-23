# Erinnerungen aufs Handy mit ntfy

Die Hantelwoche schickt Erinnerungen über die kostenlose App **ntfy** (kein Konto nötig) aufs iPhone und auf die Apple Watch.

## Einrichten (ca. 3 Minuten)

1. **Hantelwoche öffnen** (Home-Bildschirm-App) › Zahnrad oben rechts › **Benachrichtigungen** › „Einrichten“.
   Die App hat schon einen zufälligen Kanalnamen erzeugt, z. B. `hantelwoche-k7m2…`.
2. Auf **„Kanal kopieren“** tippen.
3. Im App Store **„ntfy“** installieren (Entwickler: Philipp Heckel) und öffnen. **Mitteilungen erlauben.**
4. In ntfy oben auf **+** tippen, bei „Topic name“ den Kanal einfügen, Server bleibt `ntfy.sh`, **Subscribe**.
5. Zurück in der Hantelwoche: **„Test-Nachricht senden“**. Nach ein paar Sekunden sollte „Hantelwoche ist verbunden“ kommen.
6. Haken bei **„Erinnerungen einplanen“** setzen, gewünschte Erinnerungen und Uhrzeiten wählen, **Speichern**.
   Unten unter „Eingeplant“ siehst du, was die nächsten Tage kommt.
7. Apple Watch: In der Watch-App auf dem iPhone › Mitteilungen › ntfy › „iPhone spiegeln“.

## Welche Erinnerungen gibt es?

| Erinnerung | Standard | Wann |
|---|---|---|
| Morgen-Check-in (Tagesampel) | an | 07:00, entfällt, wenn schon ausgefüllt |
| Krafttraining A/B/C | an | 30 min vor 18:00, mit Übungen, Entlastungswoche, Tagesampel |
| Bewegung und Mobility | an | 10 min vor Spaziergang, Mobility, Yoga, Ausdauer, Zirkel |
| Meditation am Abend | an | 22:00, mit Magnesium-Hinweis |
| Sonntag: Meal Prep und Wochencheck | an | 16:00 und 19:00 |
| Supplements | aus | zu den Zeiten aus dem Plan, nur was noch offen ist |
| Skill-Impuls | aus | Di, Do, Sa 17:00, wechselt zwischen deinen Skills |
| Schlafenszeit | aus | 22:30 |

Tippen auf eine Erinnerung öffnet die passende Stelle der App (Check-in, Heute, Skill …).

## Gut zu wissen

- **Die App plant bei jedem Öffnen die nächsten 2 Tage ein** (einstellbar 1–3, ntfy.sh erlaubt max. 3 Tage).
  Wer die App länger nicht öffnet, bekommt danach keine Erinnerungen mehr, bis er sie wieder öffnet.
- **Erledigt = keine Erinnerung.** Hakst du etwas ab, löscht die App die schon eingeplante Nachricht wieder.
- **Kanal geheim halten.** Wer den Namen kennt, kann mitlesen oder Nachrichten schicken. Bei Verdacht: „Neuen Kanal erzeugen“ und in ntfy neu abonnieren.
- **Ausschalten** löscht alle eingeplanten Nachrichten.
- Auf dem iPhone öffnet ein Tipp auf die Mitteilung Safari, nicht die Home-Bildschirm-App. Safari hat eigene Daten; mit GitHub-Sync sind sie dort auch da.
- Einstellungen und Kanal liegen nur auf diesem Gerät. Am besten nur auf dem Handy einschalten.

## Technik (für spätere Versionen)

- Modul im Abschnitt `BENACHRICHTIGUNGEN (ntfy)` in `index.html`: Kern `Ntfy` (Kanal, `publish`, `cancel`, `sync`) und Quellen `NTFY_TYPES[].items()`.
- Senden als JSON an `https://ntfy.sh/` ohne eigene Header (keine CORS-Vorabfrage), `delay` = Unix-Zeit, `sequence_id` = `hw-JJJJMMTT-<art>`.
  Erneutes Senden mit gleicher Kennung ersetzt die eingeplante Nachricht, `GET /<kanal>/<kennung>/delete` löscht sie.
- Lokal: `hantelwoche-v1-ntfy` (Einstellungen), `hantelwoche-v1-ntfy-plan` (was eingeplant ist).
- Deep-Links: `#go=home|today|skills|week|tpl|ex|food|progress|check|skill:<id>|ntfy`.
