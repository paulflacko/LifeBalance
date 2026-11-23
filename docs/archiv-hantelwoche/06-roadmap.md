# 06 · Roadmap

## Version 0.1 · erledigt (24.10.2026)

Alle Muss-Anforderungen aus [01-anforderungen.md](01-anforderungen.md): Tages- und Wochenansicht, Krafttraining mit Satz-Log, Pausentimer und Steigerungsvorschlag, Ersatzübungen, geführte Timer (Einstieg, Zirkel, Yoga, Mobility, Meditation, Spaziergang, Zone 2), Supplements, Ernährung, Körpergewicht mit Empfehlung, Trainingsverlauf, Sicherung. Speicherung im Claude-Konto, Offline-Datei.

## Version 0.2 · Alltagstest (nach 1–2 Trainingswochen)

Ziel: echte Nutzung auswerten und Reibung entfernen.

- [ ] Eine Woche mit der App trainieren und notieren, was stört (zu viele Taps, fehlende Infos, falsche Pausen).
- [ ] Übung tauschen in der Einheit (Goblet Squat ↔ Frontkniebeuge, Variante bei Engpass).
- [ ] RIR pro Satz optional erfassen; Steigerung auch aus RIR ableiten.
- [x] Eigene Animationen für World's Greatest Stretch, Band Pull-Aparts und alle Yoga-/Mobility-Haltungen (2026-10-26).
- [x] Platzsparende Übungen ohne Balance-Problem: Seitstütz statt Suitcase Carry, Wadenheben beidbeinig, Ausfallschritt im Stand statt gehend (2026-10-28).
- [x] Reihenfolge ohne Umstecken: Seitheben mit Band, enge Liegestütze statt French Press, „Gewichte heute“-Übersicht und Gewichtshinweis je Übung (2026-10-28).
- [x] Stangengewicht wird zu den eingetragenen Scheiben addiert (einstellbar), Empfehlungen aus den letzten 4 Einheiten: steigern, halten, leichter bei zu wenig Wdh., −10 % bei Stillstand (2026-10-28).
- [x] Abwechslung: Varianten in geraden Trainingswochen mit gleichem Gerät (2026-10-28).
- [x] Installierbare Handy-App (`handy-app/`, PWA mit Offline-Cache), Anleitung in [07-handy-start.md](07-handy-start.md) (2026-10-28).
- [x] Dienstag: Mobility nach Gefühl. Körperbereiche (Nacken bis Waden, „etwas“ oder „deutlich“) und Tagesgefühl (steif, verspannt, müde, gut) wählen, 10/15/20 min; die App stellt eine geführte Session mit Timer, Anweisungen und Animationen zusammen. Auch donnerstags als Alternative zur Standard-Routine (2026-11-02).
- [x] Handy-App liegt im GitHub-Repo `paulflacko/Hantelwoche-v1` (2026-11-02); GitHub Pages muss einmal in den Repo-Einstellungen eingeschaltet werden.
- [x] Yoga-Flow anpassen: Stil aktiv oder entspannend, Intensität sanft/mittel/kräftig, 15–45 min, optional Schwerpunkt-Körperbereiche; Standard-Flow bleibt wählbar (2026-11-03).
- [x] Online speichern: verschlüsselt (AES-GCM) im Zweig `daten` des App-Repositorys, Passwort nur auf dem Gerät (2026-11-03).
- [ ] Eigene Skizzen für Hängendes Knieheben, Rollout, Latziehen mit Band.
- [ ] Sprachansage im Zirkel („Noch 10 Sekunden“, „Als Nächstes: Burpees“) über die Sprachausgabe des Browsers.
- [ ] Notizfeld pro Einheit (z. B. „Knie zwickt“, „schlecht geschlafen“).

## Version 0.3 · Auswertung

- [ ] Diagramm pro Übung (Arbeitsgewicht über die Zeit, geschätztes 1RM).
- [ ] Sätze pro Muskelgruppe und Woche (wie das Diagramm im Plan, aber aus echten Daten).
- [ ] Wochenrückblick am Sonntag: Trainings, Meditation, Schlafschnitt, Eiweißschnitt, Gewichtstrend in einer Karte.
- [ ] Hinweis, wenn eine Übung drei Einheiten in Folge stagniert (Technik prüfen, Deload, Variante).

## Version 0.4 · Ernährung ausbauen

- [ ] Eigene Rezepte mit Nährwerten speichern (Linsen-Bolognese, Chili sin Carne, Tofu-Pfanne …).
- [ ] Meal-Prep-Planer für So: Mittagessen Mo–Mi auswählen, Einkaufsliste erzeugen.
- [ ] Optional: Nährwerte über ein Foto oder eine Beschreibung schätzen lassen (Claude-Fähigkeit `sample`, nur auf Knopfdruck).

## Version 1.0 · Erinnerungen und Installation

- [ ] PWA-Variante auf eigenem, kostenlosem Hosting (z. B. GitHub Pages) mit Service Worker, App-Symbol und echtem Offline-Betrieb.
- [ ] Push-Erinnerungen: 17:45 Training, 22:00 Meditation, 07:15 Supplements.
- [ ] Synchronisierung zwischen Artifact und PWA über die Sicherungsdatei oder einen gemeinsamen Speicher.

## Offene Fragen (aus dem Plan übernommen)

Diese Antworten würden App und Plan genauer machen:

- [ ] **Wann stehst du auf, und wie lang ist der Arbeitsweg?** Davon hängen Frühstückszeit und Eisen-Zeitpunkt in der Supplement-Liste ab.
- [ ] **Omega 3: Fischöl oder Algenöl?**
- [ ] **Etiketten von Multivitamin und Vitamin B** (B12, B6, Zink, Selen, D), um Doppelungen zu prüfen.
- [ ] **Aktuelle Blutwerte?** Entscheidet, ob Eisen und Zink in der Checkliste bleiben.
- [ ] **Ist die Klimmzugstange da?** Dann in den Einstellungen umschalten; die App nimmt automatisch die Klimmzüge statt Latziehen mit Band.
- [ ] **Startdatum:** Standard ist Montag, 26.10.2026. Bei anderem Start in den Einstellungen ändern, damit Trainingswoche, leichte Woche und Meditationsdauer stimmen.
