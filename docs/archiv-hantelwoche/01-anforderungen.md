# 01 · Anforderungen

## Ziel

Der bestehende Fitnessplan ist ein gutes Nachschlagewerk, aber beim Training selbst unpraktisch: Man scrollt zwischen Tabellen, notiert Gewichte irgendwo anders und rechnet die Steigerung im Kopf. Die App soll den Plan **im Alltag ausführbar** machen:

1. Auf einen Blick zeigen, was heute ansteht (Training, Erholung, Supplements, Essen, Meditation).
2. Durch jede Einheit führen, inklusive Timer und Animationen.
3. Gewichte und Wiederholungen speichern und daraus die nächste Steigerung ableiten (doppelte Progression).
4. Fortschritt sichtbar machen: Körpergewicht, Wochenschnitt, Arbeitsgewichte.

## Nutzer

Eine Person, trainingserfahren, keine Verletzungen. Ziel Muskel- und Gewichtsaufbau, starker Core, bessere Grundfitness. Bürojob ca. 8–17 Uhr, zeitlich flexibel. Fast vegetarisch (kein Fisch, kaum Fleisch). Schläft derzeit 6–7 h, Ziel 7,5–8 h.

## Rahmenbedingungen

| Thema | Vorgabe |
| --- | --- |
| Geräte | Handy (Hauptgerät beim Training) und Laptop |
| Equipment | Langhantel, SZ-Stange, flache Hantelbank (nicht verstellbar), Kurzhanteln, Bänder, Liegestützbrett. Klimmzugstange kommt bald. Kein Rack. |
| Zeit | Kraft Mo/Mi/Fr 18:00 (ca. 65 min mit Einstieg), Sa 09:00 Zirkel (30 min), Di/Do aktive Erholung, So Yoga + Meal Prep, täglich 22:00 Meditation |
| Sprache | Deutsch |
| Betrieb | ohne eigenen Server, ohne App-Store, ohne Kosten |
| Datenschutz | Trainings- und Körperdaten bleiben privat |

## Funktionale Anforderungen

| ID | Anforderung | Priorität |
| --- | --- | --- |
| F1 | Tagesansicht mit Zeitleiste aller Einheiten des Wochentags | Muss |
| F2 | Wochenansicht Mo–So mit Erledigt-Status, Vor- und Folgewochen | Muss |
| F3 | Krafttraining A/B/C mit Übungen, Sätzen, Wdh.-Bereich, Technik-Hinweis und Animation | Muss |
| F4 | Pro Satz Gewicht und Wiederholungen erfassen und abhaken | Muss |
| F5 | Pausentimer startet automatisch nach einem Satz (2–3 min schwer, 60–90 s sonst, kurz bei a/b-Paaren) | Muss |
| F6 | Steigerungsvorschlag aus dem letzten Training (doppelte Progression) | Muss |
| F7 | Ersatzübungen, solange keine Klimmzugstange da ist (umschaltbar) | Muss |
| F8 | Geführte Timer: Einstieg, Samstags-Zirkel (40/20 bzw. 45/15), Yoga 20/30, Mobility, Meditation mit Box-Atmung, Spaziergang, Zone 2 | Muss |
| F9 | Supplements als tägliche Checkliste nach Uhrzeit, Eisen und Zink zuschaltbar | Muss |
| F10 | Ernährung: Tagesziel kcal/Eiweiß, Beispieltag abhaken, Extras eintragen | Muss |
| F11 | Körpergewicht erfassen, Wochenschnitt, Empfehlung nach der Tabelle im Plan | Muss |
| F12 | Trainingsverlauf und Bestwerte der Grundübungen | Soll |
| F13 | Trainingswoche zählen: Meditation 5 min in Woche 1–2, Zone 2 ab Woche 5 auf 40 min, jede 7. Woche leichte Woche mit halber Satzzahl | Soll |
| F14 | Datensicherung als Datei und Wiederherstellung | Soll |
| F15 | Schlaf und Schritte pro Tag notieren | Kann |
| F16 | Erinnerungen (Push) zu Trainings- und Einnahmezeiten | Kann (später) |

## Nicht-funktionale Anforderungen

- **Bedienung beim Training:** große Tippflächen, Zahlen-Tastatur, Bildschirm bleibt an (Wake Lock), Signalton und Vibration am Ende einer Pause.
- **Lesbarkeit:** hell und dunkel, ab 360 px Breite ohne seitliches Scrollen.
- **Robustheit:** eine angefangene Einheit übersteht Neuladen und Wechsel in andere Apps.
- **Offline:** Plan und Timer funktionieren ohne Netz; die Offline-Datei kommt ganz ohne Internet aus.
- **Wartbarkeit:** Plan-Inhalte stehen als Daten an einer Stelle im Code, damit eine Planänderung eine Datenänderung ist.
- **Keine medizinische Beratung:** Supplement-Hinweise sind als Richtwerte gekennzeichnet.
