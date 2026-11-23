# Import aus der Hantelwoche

Mit diesen Skripten wurde `inhalt/` und `medien/` am 23.11.2026 einmalig aus der Hantelwoche (Stand nach Pull Request #8) erzeugt. Ab jetzt sind die Markdown-Dateien die Quelle; die Skripte sind nur zum Nachvollziehen da.

1. Den `<script>`-Teil aus `index.html` der Hantelwoche in `app.js` kopieren.
2. `node run.js app.js data.json` führt den Code in einer Sandbox aus und schreibt alle Plan-Daten (`EX`, `TIPS`, `WORKOUTS`, `SEQ`, `BR`, `PSY`, `SKILLS` …) als JSON. `extra.js` wird angehängt und rechnet die geführten Abläufe aus.
3. `python3 gen.py data.json <LifeBalance-Ordner> <Hantelwoche-Ordner>` schreibt die Markdown-Dateien und kopiert die freien Bilder.
