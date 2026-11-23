# 02 · Features

Legende: ✅ in Version 0.1 umgesetzt · 🔜 geplant (siehe [06-roadmap.md](06-roadmap.md))

## Heute

| Feature | Stand |
| --- | --- |
| Datum, Trainingswoche, Wochenstatus (Krafteinheiten x/3, Zirkel, Meditation x/7) | ✅ |
| Zeitleiste des Tages mit Start-Button je Einheit und Erledigt-Häkchen | ✅ |
| Hinweis „leichte Woche“ in jeder 7. Woche | ✅ |
| Supplements nach Uhrzeit abhaken | ✅ |
| Eiweiß- und Kalorienstand, Schlaf und Schritte | ✅ |
| Sonntags: Wochencheck-Karte | ✅ |
| Hinweis auf offene Einheit (fortsetzen) | ✅ |

## Krafttraining (Kraft A, B, C)

| Feature | Stand |
| --- | --- |
| Einstieg (10 min) als Checkliste oder geführt mit Timer | ✅ |
| Übungskarte: Nummer (1, 2, 5a/5b …), Animation, Sätze × Wdh., Technik, Equipment, Pause | ✅ |
| Satz-Zeilen mit Gewicht und Wdh., Haken setzt Satz auf erledigt | ✅ |
| Leere Wdh. beim Abhaken = obere Zielzahl, Gewicht wird in die folgenden Sätze übernommen | ✅ |
| Pausentimer mit +15 s und Weiter, Ton und Vibration | ✅ |
| Steigerungsvorschlag: „Letztes Mal … → heute +2,5 kg“ oder „Gewicht halten“ | ✅ |
| Gewicht vorbelegt mit dem Vorschlag | ✅ |
| Ersatzübungen ohne Klimmzugstange (Latziehen mit Band, Reverse Crunch) | ✅ |
| Halbe Satzzahl in der leichten Woche | ✅ |
| Einheit schließen und später fortsetzen, verwerfen, abschließen | ✅ |
| Übung tauschen (z. B. Goblet Squat ↔ Frontkniebeuge) | 🔜 |
| RIR pro Satz erfassen | 🔜 |

## Geführte Timer

| Ablauf | Inhalt | Stand |
| --- | --- | --- |
| Einstieg | Hampelmann, Katze-Kuh, World's Greatest Stretch, Dead Bug, Bird Dog, Unterarmstütz, Hüftbrücke, Pull-Aparts, Aufwärmsätze | ✅ |
| Zirkel (Sa) | 5 min Einstieg, 4 Runden × 6 Übungen 40/20 (oder 45/15), Rundenpause 1 min, 3 min Dehnen; Renegade-Row-Stufe | ✅ |
| Yoga 20 (Di) / Yoga 30 (So) | Abläufe aus dem Plan, Seiten einzeln getimt | ✅ |
| Mobility (Do) | 6 Übungen, ca. 9 min | ✅ |
| Meditation | Box-Atmung mit animiertem Quadrat, danach Body-Scan in Etappen; 5 min in Woche 1–2, sonst 10 min | ✅ |
| Spaziergang, Zone 2 | einfacher Timer, Zone 2 ab Woche 5 mit 40 min | ✅ |
| Countdown-Töne in den letzten 3 s, Bildschirm bleibt an | ✅ |
| Sprachansage der nächsten Übung | 🔜 |

## Übungen

| Feature | Stand |
| --- | --- |
| Bibliothek mit Filter: Kraft A/B/C, Einstieg, Zirkel, Mobility, Ersatzübungen | ✅ |
| Animation (32 von WorkoutLabs), Technik, Equipment, Muskelgruppe, Link zur Anleitung | ✅ |
| Renegade-Row-Stufen | ✅ |
| Eigene Animationen für Yoga, Mobility, Dehnen, WGS und Pull-Aparts (18 GIFs, img/yoga-*.gif u. a., Quelle app/yoga-animationen-quelle/) | ✅ |
| Eigene Skizzen für Knieheben, Rollout, Latziehen | 🔜 |

## Ernährung und Supplements

| Feature | Stand |
| --- | --- |
| Ziele: kcal (Standard 2.850), Eiweiß (Standard 135 g), Fett, Kohlenhydrate | ✅ |
| Beispieltag abhaken (Nährwerte geschätzt) | ✅ |
| Schnell-Einträge (Aufbau-Shake, Skyr, Whey …) und freie Einträge | ✅ |
| Tageshinweise: Ausdauertag +150–200 kcal, trainingsfreier Tag | ✅ |
| Einnahmeplan, Obergrenzen, Wechselwirkungen | ✅ |
| Eigene Rezepte und Wochen-Einkaufsliste für Meal Prep | 🔜 |

## Fortschritt

| Feature | Stand |
| --- | --- |
| Körpergewicht eintragen, Liste, Diagramm mit Wochenschnitt | ✅ |
| Empfehlung nach 2 Wochen (+200 kcal / passt / −150 kcal) | ✅ |
| Bestwerte und letzte Arbeitsgewichte der Grundübungen | ✅ |
| Trainingsverlauf mit Sätzen, Dauer, bewegtem Gewicht | ✅ |
| Diagramm pro Übung, Sätze pro Muskelgruppe und Woche | 🔜 |

## Einstellungen und Daten

| Feature | Stand |
| --- | --- |
| Start Trainingswoche 1, kcal- und Eiweißziel, Renegade-Stufe | ✅ |
| Schalter: Klimmzugstange, Zirkel 45/15, Eisen, Zink | ✅ |
| Speicherung im Claude-Konto (geräteübergreifend) mit lokaler Kopie | ✅ |
| Sicherung als JSON-Datei, Sicherung laden, alles löschen (mit Bestätigung) | ✅ |

## User Stories (Auswahl)

- *Als P möchte ich nach der Arbeit auf „Training starten“ tippen und sofort sehen, mit welchem Gewicht ich heute anfange*, damit ich nicht in alten Notizen suchen muss.
- *Als P möchte ich nach jedem Satz nur einen Haken setzen*, und die Pause läuft automatisch.
- *Als P möchte ich samstags den Zirkel starten und das Handy weglegen*, weil Töne Arbeit und Pause ansagen.
- *Als P möchte ich sonntags sehen, ob meine Zunahme im Ziel liegt*, und eine klare Ansage bekommen, ob ich mehr essen soll.
- *Als P möchte ich abends die Meditation mit Atemführung starten*, statt eine zusätzliche App zu brauchen.
