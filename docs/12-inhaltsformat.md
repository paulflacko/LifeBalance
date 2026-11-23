# 12 · Inhaltsformat

Alle Inhalte liegen als Markdown-Dateien in [inhalt/](../inhalt/README.md), **eine Datei pro Eintrag**. Jede Datei hat zwei Teile:

1. **Kopf (YAML-Frontmatter)** zwischen `---`: feste Felder, die die App auswertet (Filter, Suche, Verweise).
2. **Text** darunter: lesbares Markdown mit festen Überschriften, die die App als Abschnitte anzeigt.

Der **Dateiname ist die ID** (`inhalt/uebungen/deadlift.md` → `deadlift`). IDs ändern sich nie, weil Abläufe, Skills und Nutzerdaten darauf verweisen. Die IDs stammen aus der Hantelwoche, damit alte Trainingsdaten weiter passen.

## Gemeinsame Felder

| Feld | Pflicht | Bedeutung |
|---|---|---|
| `id` | ja | gleich dem Dateinamen |
| `name` | ja | Anzeigename |
| `typ` | ja | `uebung`, `atemuebung`, `selbsthilfe`, `skill`, `ablauf`, `baukasten`, `wochenvorlage`, `beispieltag`, `supplementplan`, `check-in-skript` |
| `saeule` | ja | `koerper`, `erholung`, `ernaehrung`, `geist`, `wachstum` |
| `tags` | nein | freie Schlagworte |

Alle festen Schlüssel (Kategorien, Equipment, Methoden …) stehen in [inhalt/verzeichnisse.md](../inhalt/verzeichnisse.md).

## Übung (`typ: uebung`)

```markdown
---
id: "deadlift"
name: "Kreuzheben"
typ: "uebung"
saeule: "koerper"
art: "kraft"                 # kraft | core | kondition | mobility | yoga
kategorie: "beine"
equipment: ["lh"]
equipment_text: "Langhantel"
muskeln: "Po, Beinbeuger, Rücken"
einheit: "kg"                # kg | bw | band | sec | carry
steigerung_kg: 2.5
hantel: "lh"                 # lh | sz | kh | kh2 (für Stangengewicht)
pro_seite: true              # nur wenn zutreffend
braucht_klimmzugstange: true # nur wenn zutreffend
foto: "../../medien/fotos/barbell_deadlift.webp"
foto_hinweis: "Foto mit Kettlebell, Ablauf mit Kurzhantel gleich"
animation: "../../medien/animationen/yoga-taube.gif"
bild_fehlt: true             # wenn weder Foto noch Animation
---

# Kreuzheben

![…](../../medien/fotos/barbell_deadlift.webp)

> Kurzer Technik-Hinweis in einem Satz.

- **Muskeln/Bereich:** …

## Ausführung
## Häufige Fehler
## Atmung
## Wo du es spürst
## Kommt vor in
```

`## Kommt vor in` wird beim Erzeugen aus Abläufen und Skills berechnet und nicht von Hand gepflegt.

## Atemübung (`typ: atemuebung`)

Felder: `ziel` (ruhe, fokus, energie), `evidenz` (stark, mittel, trad), `einsatz` (Liste), `dauer_standard`, `dauer_optionen`, `dauer_einheit`, `sicherheitshinweis`.
Abschnitte: Wann, So geht es, Varianten und Rhythmus, Wirkung, Quellen.

Ein Rhythmus steht als Zeile „Einatmen 4 s → Halten 4 s → Ausatmen 4 s → Leer halten 4 s“. Beim Bau der App wird dafür ein maschinenlesbares Feld `rhythmen` ergänzt.

## Selbsthilfe (`typ: selbsthilfe`)

Felder: `methode`, `einsatz` (Anliegen), `dauer_min`, `evidenz`, `hat_formular`.
Abschnitte: Warum es hilft, Ablauf (Tabelle Schritt und Zeit), Eintrag danach (Formularfelder), Quelle, Krisenhinweis.

## Skill (`typ: skill`)

Felder: `bereich` (kg, ger, mob, geist), `belastung` (1–3), `koerperbereich`, `stufen`, `misst_automatisch` (med, breath, focus, read).
Abschnitte: Stufen (je Stufe Ziel, Test, Übungen, Hinweis), Technik, Häufige Fehler, Hilfsübungen, Einbau in die Woche, Sicherheit.

## Ablauf (`typ: ablauf`)

Felder: `art` (krafttraining, gefuehrt, Kraft, Core, Ausdauer, Calisthenics), `modus` (saetze, runden), `mit_einstieg`, bei Runden `runden`, `arbeit_s`, `pause_s`, `rundenpause_s`, bei geführten `schritte`, `dauer_s`.
Text: Tabelle der Übungen bzw. Schritte, Übungen als Link auf ihre Datei.

## Weitere

- `baukasten`: Pools für Mobility und Yoga nach Gefühl.
- `wochenvorlage`: Tage mit Blöcken (Zeit, Name, Details, startet).
- `beispieltag`, `supplementplan`: Tabellen mit Zeit, Menge, kcal, Eiweiß.
- `check-in-skript`: Fragen mit Schlüsseln und Antworten, Ablauf als Diagramm.

## Regeln für neue Inhalte

- Texte in eigenen Worten, auf Deutsch, Du-Form, kurze Sätze.
- Bilder nur mit freier Lizenz, Herkunft in [LIZENZEN.md](../LIZENZEN.md) eintragen.
- Studienangaben mit Autor, Jahr, Zeitschrift.
- Keine persönlichen Daten in Inhalten.
