# Quellen und Lizenzen

Stand: 23.11.2026. Übersicht, woher Bilder und Inhalte in LifeBalance stammen und unter welchen Bedingungen sie genutzt werden. Übernommen aus der Hantelwoche und an die neue Ablage angepasst.

## Übungsbilder

| Bilder | Wo | Quelle | Lizenz |
|---|---|---|---|
| 191 Fotos (Start und Ende, als kleine Animation) | `medien/fotos/*.webp` | [free-exercise-db](https://github.com/yuhonas/free-exercise-db) von yuhonas, aufbauend auf [exercises.json](https://github.com/wrkout/exercises.json) | [Unlicense](https://unlicense.org/): gemeinfrei, Nutzung, Änderung und Weitergabe ohne Bedingungen |
| 32 eigene Animationen (Yoga, Mobility, Einstieg) | `medien/animationen/*.gif` | Selbst erstellt mit Python/Pillow, Quellcode in `werkzeuge/animationen/` | Eigene Werke, frei nutzbar ([CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.de)) |

**Nicht übernommen:** 42 gezeichnete Animationen von [WorkoutLabs](https://workoutlabs.com/exercise-guide/) aus der ersten Version der Hantelwoche. Sie sind nicht frei lizenziert und gehören nicht in ein öffentliches Repository. 75 Übungen haben vorerst kein freies Bild (bei einigen gab es nur eine solche Zeichnung, bei anderen noch nie ein Bild) (`bild_fehlt: true` im Kopf der Datei, Liste in [inhalt/uebungen/README.md](inhalt/uebungen/README.md)).

Bearbeitung der Fotos: auf 480 × 320 Pixel verkleinert, Markierung 1 (Start) und 2 (Ende) eingezeichnet, als WebP-Animation (1,4 s je Bild) gespeichert. Werkzeug: `werkzeuge/fotos/mkphotos.py`.

Wenn ein Foto ein anderes Gerät zeigt als beschrieben (Kettlebell statt Kurzhantel, Kabelzug statt Band), steht das im Feld `foto_hinweis`.

### Geprüft, aber nicht genutzt
- **wger** (wger.de, Bilder meist CC BY-SA 3.0/4.0 mit Namensnennung je Bild): von dieser Umgebung aus nicht erreichbar, zudem müsste jede Urheberin einzeln genannt werden.
- **Wikimedia Commons** (u. a. Everkinetic-Grafiken, CC BY-SA 3.0): von hier nicht erreichbar. Kandidat für später, besonders für Yoga-Fotos.

## Selbsthilfe-Übungen „Kopf und Gefühle“

Alle 25 Übungen sind **in eigenen Worten** beschrieben. Es wurden keine Arbeitsblätter oder Texte übernommen, nur die dahinterliegenden, frei beschriebenen Methoden. Jede Übung nennt ihre Quelle in ihrer Datei unter `inhalt/selbsthilfe/`.

| Methode | Übungen | Grundlage |
|---|---|---|
| Kognitive Verhaltenstherapie (KVT) | Gedankenprotokoll, Denkfallen, Sorgenzeit, Problemlösen, Aktivitäten planen, Mit den Augen eines Freundes, Wenn-dann-Plan | A. T. Beck; D. Burns; T. D. Borkovec (Sorgenzeit, 1983); D’Zurilla und Goldfried (Problemlösen); Lewinsohn, Martell und Jacobson (Verhaltensaktivierung); P. M. Gollwitzer (Wenn-dann-Pläne) |
| ACT (Akzeptanz- und Commitment-Therapie) | Anker werfen, Abstand zu Gedanken, Blätter auf dem Fluss, Einem Gefühl Raum geben, Werte-Kompass | S. C. Hayes; R. Harris; WHO „Doing What Matters in Times of Stress“ (2020) |
| DBT-Skills | STOP, TIPP, Gefühle benennen, Entgegengesetzt handeln, Radikale Akzeptanz | M. Linehan, DBT Skills Training Manual; Lieberman et al. 2007 (Affect Labeling) |
| Achtsamkeit und Entspannung | 5-4-3-2-1, Progressive Muskelentspannung, Body Scan, Achtsames Gehen | E. Jacobson (1938), Bernstein und Borkovec; J. Kabat-Zinn (MBSR); Thich Nhat Hanh |
| Selbstmitgefühl | Selbstmitgefühls-Pause | K. Neff, C. Germer (Mindful Self-Compassion) |
| Positive Psychologie | Drei gute Dinge | M. Seligman et al. 2005 |
| Schlaf | Bett ist zum Schlafen da | R. Bootzin (Stimuluskontrolle); S3-Leitlinie Schlafstörungen der DGSM |

Frei lizenzierte Leitfäden, die als Hintergrund dienten und sich zum Weiterlesen eignen:
- WHO (2020): *Doing What Matters in Times of Stress: An Illustrated Guide*. Lizenz CC BY-NC-SA 3.0 IGO. Auch auf Deutsch erhältlich.
- WHO (2016): *Problem Management Plus (PM+)*. Lizenz CC BY-NC-SA 3.0 IGO.

Die Evidenz-Einstufung („Viele Studien“, „Einzelne Studien“) ist eine grobe Orientierung, dieselbe wie bei den Atemübungen.

**Wichtig:** Die Übungen sind Selbsthilfe und ersetzen keine Diagnose oder Behandlung. Jede Übung zeigt den Hinweis auf Hilfe in Krisen (Telefonseelsorge 0800 111 0 111 und 0800 111 0 222, Notruf 112, Terminservice 116 117).

## Texte

Übungsbeschreibungen, Technik-Tipps, Atemübungen, Skills und Pläne sind eigene Texte aus der Hantelwoche. Quellenangaben zu Studien stehen bei der jeweiligen Atemübung und Selbsthilfe-Übung.
