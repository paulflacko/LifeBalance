# 02 · Navigation

Entschieden am 23.11.2026: **Aufgaben-Modell** mit vier Tabs. Die Tabs folgen den vier Dingen, die man mit der App tut: den Tag leben, festlegen was ansteht, sehen wie es läuft, nachschlagen.

```
┌──────────────────────────────────────┐
│ Montag, 23. November   ⌕  (P)        │  ← Suche und Profil oben rechts, auf jeder Seite
│                                      │
│              Inhalt                  │
│                                      │
├──────────────────────────────────────┤
│ Heute   Plan   (+)  Fortschritt Wissen│  ← vier Tabs, Plus-Knopf in der Mitte
└──────────────────────────────────────┘
```

| Tab | Frage | Reiter |
|---|---|---|
| **Heute** | Was ist jetzt dran? | Tag · Woche |
| **Plan** | Was steht an, womit? | Woche (Wochenvorlage bearbeiten) · Abläufe (Workouts, Yoga, Mobility, Atmung, Meditation, Routinen) · Ernährung (Ziele, Beispieltag, Rezepte, Supplements) |
| **Fortschritt** | Wie läuft es? | Überblick (fünf Säulen) · Skills · Ziele · Rückblick |
| **Wissen** | Wie geht das? | Suche, Kategorien, Favoriten |

Verworfen wurden: A (Heute, Bereiche, Ziele, Wissen; jede Säule als eigene Seite) und C (nur drei Tabs: Heute, Bereiche, Ich).

## Plus-Knopf

Von jedem Tab aus in zwei Taps etwas **erfassen** oder **starten**. Öffnet ein Blatt von unten:

- **Erfassen:** Mahlzeit, Supplements, Schlaf, Gewicht, Stimmung, Notiz, Wasser, eigene Tracker.
- **Starten:** Workout, Atmung, Meditation, Lesen, Fokus, Mobility nach Gefühl, Selbsthilfe („Kopf frei“).

Die Kacheln sind frei belegbar. Eigene Tracker erscheinen automatisch.

## Oben rechts

- **Lupe:** globale Suche über Übungen, Atemtechniken, Yoga, Skills, Selbsthilfe, Rezepte, Ratgeber. Treffer öffnen die Wissenskarte.
- **Profilbild:** Profil, Einstellungen, Equipment, Module ein- und ausschalten, Startseite anpassen, Erinnerungen, Sync und Sicherung.

## Was aus den alten Tabs wird

| Hantelwoche | LifeBalance |
|---|---|
| Tab Start | Heute (wird die Startseite) |
| Tab Heute (Tagesplan, Supplements, Schlaf, Schritte, Wochencheck) | Heute › Tag; Wochencheck → Fortschritt › Rückblick |
| Tab Woche | Ansehen: Heute › Woche; Bearbeiten: Plan › Woche |
| Tab Workouts (Vorlagen, Editor, Plan A/B/C) | Plan › Abläufe, Filter Körper |
| Tab Übungen (Bibliothek) | Wissen › Übungen |
| Tab Ernährung | Plan › Ernährung; Tageswerte in Heute; Eintragen über Plus |
| Tab Fortschritt | Fortschritt › Überblick, je Säule aufklappbar |
| Tab Skills | Fortschritt › Skills |
| Kachel Tagesampel | Heute oben; Verlauf in Fortschritt (Filter Erholung) |
| Kachel Regeneration heute | Heute › Schnellstart; Plan › Abläufe (Filter Erholung) |
| Kacheln Mobility nach Gefühl, Yoga-Flow | Plan › Abläufe (Filter Körper); Start auch über Plus |
| Kachel Atemübungen | Plan › Abläufe (Filter Erholung); Techniken in Wissen |
| Kacheln Meditation, Fokusblock | Plan › Abläufe (Filter Geist); Start über Plus |
| Kachel Lese-Timer, Bücher | Start über Plus; Bücher in Fortschritt › Ziele |
| Karte und Kachel „Kopf frei“ | Plus › Starten; Übungen in Wissen (Filter Geist) |
| Einstellungen, GitHub-Sync, Sicherung | Profilbild oben rechts |

## Deep-Links

Jeder Bildschirm hat eine Adresse, damit Erinnerungen und Kurzbefehle direkt dorthin springen: `#heute`, `#heute/woche`, `#plan/abläufe`, `#fortschritt/skills`, `#wissen/uebung/<id>`, `#start/<ablauf-id>`, `#checkin`, `#erfassen/<tracker>`.
