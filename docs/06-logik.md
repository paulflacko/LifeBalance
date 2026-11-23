# 06 · Logik

Die Regeln, nach denen die App rechnet und vorschlägt. Alle stammen aus der Hantelwoche und haben sich dort bewährt; Änderungen gegenüber der Hantelwoche sind markiert.

## Tagesampel

Check-in-Skript: [inhalt/check-ins/tagesampel.md](../inhalt/check-ins/tagesampel.md).

### Reihenfolge der Fragen

`rec → cause → sick → sleep → sore → areas → pain → stress → motiv → Ergebnis`

Übersprungen wird:
- `cause`, wenn Erholung (`rec`) 3 oder mehr ist,
- `sick`, wenn bei `cause` nicht „krank“ gewählt ist,
- `areas`, wenn kein Muskelkater oder Schmerz (`sore` = 0),
- `pain`, wenn `sore` nicht 3 ist („Schmerz, der sich anders anfühlt“).

### Punktzahl (0 bis 100)

| Anteil | Rechnung | max. |
|---|---|---|
| Erholung | (rec − 1) / 4 × 35 | 35 |
| Schlaf | mit Stunden: clamp((h − 5) / 3, 0, 1) × 20; ohne Angabe: 13, bei Ursache „Schlaf“ 6 | 20 |
| Muskelkater | sore 0/1/2/3 → 15/11/5/0 | 15 |
| Stress | (5 − stress) / 4 × 15 | 15 |
| Lust | (motiv − 1) / 4 × 15 | 15 |
| Ruhepuls | über der Basis (Median 21 Tage): ≥ 7 → −12; ≥ 4 → −6 | |

Ampel: **Grün** ab 60, **Gelb** ab 30, sonst **Rot**.

Korrekturen danach:
- krank mit Beschwerden im Körper → Rot,
- krank nur oberhalb des Halses und Grün → Gelb,
- Schmerz, der bei Belastung stärker wird, und Grün → Gelb,
- „völlig platt“ (rec = 1) und Grün → Gelb.

Gründe als kurze Sätze: „kurzer Schlaf (5,5 h)“, „deutlicher Muskelkater“, „hoher Stress“, „wenig Lust“, „Ruhepuls 8 über deinem Schnitt“.

### Folgen

- **Grün:** Plan wie geplant.
- **Gelb:** Angebot „leichte Variante“: 2/3 der Sätze (aufgerundet) mit 90 % des vorgeschlagenen Gewichts.
- **Rot:** Erholung zuerst: Vorschlag sanfte Mobility, Atemübung, Spaziergang statt Training.
- Genannte Körperbereiche fließen in „Regeneration heute“ ein (Gewicht 2).
- *Neu in LifeBalance:* bei hohem Stress zusätzlich eine passende Atemübung oder Selbsthilfe-Übung in „Passend zu heute“.

## Steigerungsvorschlag

Für jede Übung in einer Krafteinheit, aus den letzten 4 Einheiten mit derselben Übung. Ziel: doppelte Progression, Sätze enden bei RIR 2.

**Mit Gewicht** (Einheit `kg` oder `carry`):

1. Noch nie gemacht → „Gewicht wählen, mit dem du die untere Wdh.-Zahl mit RIR 2 schaffst.“
2. Letztes Mal alle Sätze mit der oberen Wdh.-Zahl → **+`steigerung_kg`**.
3. Letztes Mal ein Satz unter der unteren Zahl → **leichter:** − max(Schritt, 5 %), gerundet auf den Schritt.
4. Drei Einheiten gleiches Gewicht, nie oben angekommen, Wdh.-Summe nicht gestiegen → **Plateau:** −10 %, neu aufbauen, Hinweis auf Schlaf und Essen.
5. Sonst → Gewicht halten, Ziel: jede Wdh.-Zahl +1 (bis zur oberen Grenze).

Stangengewicht (Langhantel, SZ, Kurzhantelgriff) wird auf Wunsch addiert; eingetragen werden nur die Scheiben.

**Ohne Gewicht:** Liegestütze ab 20 Wdh. → Rucksack mit Gewicht. Halteübungen (`sec`) → 5 s länger, bei oberer Zeit nächste Variante. Sonst obere Zahl erreicht → schwerere Variante oder stärkeres Band.

**Varianten in geraden Wochen:** Manche Übungen im Plan haben eine Variante (`v`), die in geraden Trainingswochen genommen wird. **Ersatz ohne Klimmzugstange:** `alt`, solange im Profil keine Stange vorhanden ist.

## Regeneration heute

Schlägt nach Training eine kurze Mobility-Einheit für die belasteten Bereiche vor.

1. Für die letzten 4 Tage (heute, gestern, vorgestern, vor 3 Tagen; Gewicht 1 / 1 / 0,6 / 0,3) alle abgeschlossenen Einheiten nehmen.
2. Jede Übung belastet Bereiche nach ihrem Feld `muskeln` und der Tabelle in [koerperbereiche.md](../inhalt/mobility/koerperbereiche.md#belastung-aus-dem-training), mal Anzahl der Sätze. Zirkel zählt wie 4 Sätze seiner 6 Übungen, Ausdauer belastet Waden, Hüfte, Beinrückseite.
3. Die 4 stärksten Bereiche mit Summe ≥ 1: ab 7 Gewicht 2, ab 2,5 Gewicht 1.
4. Bereiche aus dem Check-in bekommen Gewicht 2.
5. Kein Training erfasst → Büro-Fokus: Hüfte, oberer Rücken, Nacken.
6. Gefühl: Schlaf unter 6 h oder Ampel Rot → „Müde“; Training in den letzten 2 Tagen und Summe ≥ 25 → „Verspannt“; sonst „Ganz gut“.
7. Dauer: zuletzt gewählte (Standard 15 min). Daraus Mobility nach Gefühl.

## Mobility nach Gefühl

Eingaben: Bereiche (Gewicht 1 oder 2, oder keine = alle), Gefühl, Minuten. Baukasten: [koerperbereiche.md](../inhalt/mobility/koerperbereiche.md).

1. **Öffner:** sanft → Fersensitz 60 s; sonst Katze-Kuh 60 s.
2. **Abschluss:** sanft oder verspannt → Endentspannung (150 bzw. 90 s); sonst Kindhaltung 60 s.
3. Pro Bereich eine Warteschlange aus seinem Pool. Gefühl „Steif“: bewegte Übungen zuerst; „Müde“: anstrengende (WGS, Bird Dog, Pull-Aparts) ans Ende; sonst wöchentlich wechselnder Start im Pool.
4. Kosten einer Übung: Zeit × Haltefaktor des Gefühls (bewegte Übungen ohne Faktor) × 2 bei Seitenwechsel.
5. Reihum (Bereiche mit Gewicht 2 doppelt so oft) die nächste noch nicht benutzte Übung nehmen, solange Zeit übrig ist (20 s Toleranz).
6. Bleibt viel Zeit: mit benachbarten Bereichen auffüllen, dann Haltezeiten verlängern.
7. Reihenfolge nach Position: stehend → Ausfallschritt → Vierfüßler → sitzend/kniend → liegend, damit man nicht ständig aufsteht.

**Yoga nach Gefühl** funktioniert gleich, mit [Yoga-Baukasten](../inhalt/mobility/yoga-baukasten.md), Stil (Aktiv/Entspannend) und Intensität (Faktor 0,8 / 1 / 1,25).

## Atem-Player

Rhythmus aus Phasen: Bereit machen, Einatmen, Nachatmen, Halten, Ausatmen, Leer halten, Luft anhalten, Frei atmen. Jede Atemübung hat Varianten mit festen Sekunden ([inhalt/atmung/](../inhalt/atmung/README.md)) und Dauer-Optionen. Der Player wiederholt das Muster bis zur gewählten Dauer.

Vorschlag nach Tageszeit und Einsatzzweck (Einschlafen, akuter Stress, vor Termin, Fokus, Energie, nach dem Training, Grübeln, Atemkontrolle). Wim-Hof erst nach Bestätigung der Sicherheitshinweise.

## Skills

Jeder Skill hat Stufen mit einem Test (`reps`, `hold`, `kgbw`, `kg`, `cm`, `sess`, `book`). Ein eingetragener Testwert ≥ Ziel → Stufe bestanden, nächste wird frei. Abläufe zählen automatisch für Skills mit `misst_automatisch` (Meditation, Atemkontrolle, Fokus, Lesen): z. B. „7 Einheiten mit mindestens 5 min“.

## Entlastung und Trainingswoche

Jede 7. Trainingswoche: halbe Satzzahl. Meditation 5 min in Woche 1–2, Zone 2 ab Woche 5 länger (siehe [Datenmodell](05-datenmodell.md#abgeleitete-werte-nicht-gespeichert)).

## Laufende Timer

Eine angefangene Einheit, ein Fokusblock oder eine Lese-Session übersteht Neuladen und App-Wechsel (Startzeit gespeichert, Restzeit aus der Uhr berechnet).
