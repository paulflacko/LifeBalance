> **Archiv.** Die Dokumente der ersten Version (Hantelwoche, Repo [Hantelwoche-v1](https://github.com/paulflacko/Hantelwoche-v1)), unverändert übernommen, damit Entscheidungen nachvollziehbar bleiben. Pfade wie `../app/` beziehen sich auf die alte Ablage. Gültig für LifeBalance ist [docs/](../README.md).

# Hantelwoche – interaktive App zum Fitnessplan

Hantelwoche macht aus dem Fitnessplan („Fitnessplan: Training, Ernährung, Supplements“) ein Programm, das beim Training auf dem Handy und am Laptop mitläuft: Es zeigt, was heute dran ist, führt durch jede Einheit, merkt sich Gewichte und Wiederholungen und schlägt die nächste Steigerung vor.

## Öffnen

| Weg | Wofür | Daten |
| --- | --- | --- |
| **App-Link** (claude.ai Artifact) | Normalfall, Handy und Laptop | in deinem Claude-Konto, privat, auf allen Geräten gleich |
| **`hantelwoche-offline.html`** | ohne Internet, z. B. am Laptop | nur in diesem Browser; per „Daten als Datei sichern“ übertragbar |

Tipp fürs Handy: Den App-Link im Browser öffnen und „Zum Startbildschirm hinzufügen“ wählen, dann startet die App wie eine normale App.

## Inhalt dieses Ordners

| Datei | Inhalt |
| --- | --- |
| [01-anforderungen.md](01-anforderungen.md) | Ziel, Nutzer, Rahmenbedingungen, funktionale und nicht-funktionale Anforderungen |
| [02-features.md](02-features.md) | Feature-Liste mit Priorität und Stand, User Stories |
| [03-datenmodell.md](03-datenmodell.md) | Plan-Daten (fest) und Nutzerdaten (Einträge), mit JSON-Beispielen |
| [04-architektur.md](04-architektur.md) | Technik-Entscheidung, Speicherung, Offline, Alternativen |
| [05-screens-und-ablaeufe.md](05-screens-und-ablaeufe.md) | Bildschirme und die wichtigsten Abläufe |
| [06-roadmap.md](06-roadmap.md) | Versionen, nächste Schritte, offene Fragen |
| [07-handy-start.md](07-handy-start.md) | App auf dem Handy ohne Claude starten |
| `../app/index.html` | Quellcode der App (eine Datei, kein Build nötig) |
| `../app/img/` | 32 Übungsanimationen (WorkoutLabs) |
| `../app/build_offline.py` | baut die Offline-Datei mit eingebetteten Animationen |
| `../app/build_pwa.py` | baut die installierbare Handy-App nach `../handy-app/` |

## Stand

Version 0.1 (24.10.2026): alle MVP-Funktionen aus [02-features.md](02-features.md) sind umgesetzt und auf Handy- und Laptop-Breite getestet. Was als Nächstes kommt, steht in [06-roadmap.md](06-roadmap.md).
