# LifeBalance

*Arbeitsname.* Eine persönliche Planungs-, Lebens- und Verbesserungs-App. Sie ist der Nachfolger der [Hantelwoche](https://github.com/paulflacko/Hantelwoche-v1), die als Trainings-App begann und zu einem Werkzeug für Training, Erholung, Atmung, Meditation, Fokus, Lesen und Skills gewachsen ist.

LifeBalance stellt nicht mehr die Frage „Was trainiere ich?“, sondern **„Wie geht es mir, was ist heute dran, woran wachse ich?“**. Fitness ist eine von fünf Säulen: **Körper, Erholung, Ernährung, Geist, Wachstum**.

## Stand

Dieses Repository enthält **noch keinen App-Code**. Es besteht aus zwei Teilen:

1. **Die Funktion, beschrieben in Markdown** ([docs/](docs/README.md)): Vision, Säulen, Navigation, Bildschirme, Bausteine, Datenmodell, Logik, Roadmap. Daraus wird die App gebaut.
2. **Alle Inhalte aus der Hantelwoche** ([inhalt/](inhalt/README.md), [medien/](medien/)), umgezogen in ein einheitliches Format: eine Markdown-Datei pro Übung, Atemtechnik, Selbsthilfe-Übung, Skill und Ablauf, mit festen Feldern im Kopf und lesbarem Text darunter. Die App liest später genau diese Dateien.

## Aufbau

| Ordner | Inhalt |
|---|---|
| [docs/](docs/README.md) | Spezifikation der App (Was sie tun soll und wie) |
| [docs/archiv-hantelwoche/](docs/archiv-hantelwoche/README.md) | Dokumente der ersten Version, zum Nachlesen |
| [inhalt/](inhalt/README.md) | Wissen und Pläne: Übungen, Atmung, Selbsthilfe, Skills, Abläufe, Wochenplan, Ernährung, Check-ins |
| [medien/fotos/](medien/fotos/) | 191 Übungsfotos (Start und Ende), gemeinfrei |
| [medien/animationen/](medien/animationen/) | 32 eigene Animationen für Yoga, Mobility und Einstieg |
| [werkzeuge/](werkzeuge/README.md) | Python-Skripte, mit denen Fotos und Animationen erzeugt wurden |
| [LIZENZEN.md](LIZENZEN.md) | Herkunft und Lizenz aller Bilder und Texte |

## Mitmachen und ändern

Jede Datei lässt sich direkt auf GitHub lesen und bearbeiten. Eine neue Übung ist eine neue Datei in `inhalt/uebungen/`, aufgebaut wie die anderen (siehe [Inhaltsformat](docs/12-inhaltsformat.md)).

Die Inhalte sind Selbsthilfe und Trainingswissen, keine medizinische oder therapeutische Beratung.
