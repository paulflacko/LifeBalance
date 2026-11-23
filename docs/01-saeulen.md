# 01 · Die fünf Säulen

Jede Säule beantwortet eine Frage und sammelt die Module, die dazu gehören. Säulen sind **kein eigener Tab**, sondern Farbe und Filter, die überall gleich wirken: Ringe auf der Startseite, Filter-Chips im Plan, Überblick im Fortschritt, Kategorien im Wissen.

Schlüssel in den Inhaltsdateien: `saeule: koerper | erholung | ernaehrung | geist | wachstum`.

| Säule | Frage | Vorhanden (aus der Hantelwoche) | Neu |
|---|---|---|---|
| **Körper** | Bin ich stark und beweglich? | Krafttraining A/B/C, Workout-Editor und 16 Vorlagen, Zirkel, Mobility nach Gefühl, Yoga-Flows, 290 Übungen, Körpergewicht | Schritte und Ausdauer aus Apple Health, Körpermaße (optional) |
| **Erholung** | Bin ich erholt? | Tagesampel (Check-in), Regeneration heute, 12 Atemtechniken, Schlaf | Ruhepuls und HRV aus Health, Schlafverlauf |
| **Ernährung** | Versorge ich mich gut? | Kalorien und Eiweiß, Beispieltag, Snacks, Supplements nach Uhrzeit | Rezepte, Meal Prep mit Einkaufsliste, Wasser, Koffein |
| **Geist** | Bin ich ruhig und klar? | Meditation (geführt, in Stufen), Fokusblock, 24 Selbsthilfe-Übungen „Kopf und Gefühle“ | Stimmung, Journal, Dankbarkeit, Abendrückblick |
| **Wachstum** | Komme ich voran? | Skillbank (30 Skills mit Stufen), Lese-Timer und Bücher | Eigene Ziele, Gewohnheiten, Lernen mit Karteikarten |

## Wie eine Säule sich zeigt

- **Farbe:** jede Säule hat eine feste Farbe (Festlegung im Design, z. B. Körper Orange, Erholung Blau, Ernährung Grün, Geist Violett, Wachstum Gelb).
- **Ring auf der Startseite:** Tageserfüllung der Säule aus ihren Wochenzielen (z. B. Körper: geplanter Block erledigt; Geist: Meditation erledigt).
- **Chip als Filter:** „Alle · Körper · Erholung · Ernährung · Geist · Wachstum“ oben in Plan, Fortschritt und Wissen. Ein Tipp auf „Körper“ zeigt im Plan die Trainingsvorlagen, im Fortschritt die Kraftwerte, im Wissen die Übungen.
- **Zeile im Fortschritt:** pro Säule der Wochenstand und der wichtigste Wert.

## Zuordnung der vorhandenen Inhalte

| Inhalt | Säule | Hinweis |
|---|---|---|
| Übungen, Kraft-Abläufe, Vorlagen, Yoga, Mobility | Körper | |
| Atemübungen | Erholung | Feld `ziel` unterscheidet Beruhigen, Fokus, Aktivieren |
| Tagesampel | Erholung | |
| Meditation (geführter Ablauf) | Geist | |
| Selbsthilfe-Übungen | Geist | |
| Skills | Wachstum | Feld `bereich` sagt, ob körperlich oder geistig |
| Beispieltag, Supplements | Ernährung | |

Ein Inhalt hat genau eine Hauptsäule. Querbezüge (Atemübung „Kapalabhati“ aktiviert auch den Körper) laufen über Tags, nicht über eine zweite Säule.
