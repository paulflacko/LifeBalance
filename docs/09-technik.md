# 09 · Technik

Rahmen: ohne eigenen Server, ohne App-Store, ohne Kosten, Deutsch, Handy zuerst.

## Plattform

**Progressive Web-App auf GitHub Pages**, wie die Hantelwoche: Website, die sich auf dem iPhone zum Home-Bildschirm hinzufügen lässt, offline funktioniert und sich wie eine App anfühlt. Push über Pages auf GitHub `main` aktualisiert die App.

Anders als die Hantelwoche (eine Datei mit über 500 KB):

- **Aufgeteilt in Module:** Kern (Navigation, Speicher, Bausteine), je Säule bzw. Modul eine Datei, Styles getrennt. Möglichst weiterhin ohne Build-Schritt (ES-Module im Browser); ein kleiner Build ist erlaubt, wenn er die Inhalte bündelt.
- **Inhalte als Daten:** Die Markdown-Dateien in [inhalt/](../inhalt/README.md) sind die Quelle. Ein Skript wandelt sie beim Veröffentlichen in eine kompakte JSON-Datei pro Inhaltstyp um (Kopf als Felder, Abschnitte als Text). Die App lädt Wissen erst, wenn es gebraucht wird.
- **Modul-Register:** Jedes Modul meldet sich mit Säule, Karten, Plus-Kacheln, Eintragsarten, Kennzahlen und Erinnerungen an. Startseite, Plus-Menü, Plan und Fortschritt bauen sich daraus auf.

Offen: Framework oder reines JavaScript ([Offene Fragen](11-offene-fragen.md)).

## Speicherung

- **Auf dem Gerät:** IndexedDB (statt eines großen localStorage-Eintrags), damit viele Einträge schnell bleiben.
- **Sicherung als Datei:** Export und Import aller Nutzerdaten als JSON. Vor jeder Übernahme und jedem großen Update automatisch.

## Sync zwischen Handy und Laptop

Wie in der Hantelwoche: Nutzerdaten werden **verschlüsselt** (AES-GCM, Schlüssel aus einem Passwort, das nur auf den Geräten liegt) in einen eigenen Zweig `daten` eines GitHub-Repositorys geschrieben, mit einem Fine-grained Token, das nur dieses Repo darf. Abgleich beim Start, beim Zurückkehren in die App und wenige Sekunden nach jeder Änderung. Pro Dokument gewinnt der neuere Stand.

Damit das öffentliche Repo nichts Persönliches zeigt, kann der Zweig `daten` in einem **eigenen privaten Repo** liegen (Einstellung im Profil).

## Offline

Service Worker hält App, Inhalte und Bilder im Cache. Abläufe und Timer funktionieren ohne Netz. Bilder (ca. 12 MB) werden beim ersten Öffnen einer Kategorie nachgeladen, nicht alle beim Start.

## Bedienung

- Große Tippflächen, Zahlen-Tastatur für Gewichte, Bildschirm bleibt während Abläufen an (Wake Lock), Ton und Vibration am Ende einer Pause.
- Hell und dunkel, ab 360 px Breite ohne seitliches Scrollen.
- Bildstil wählbar: Fotos für Kraft, eigene Animationen für Yoga und Mobility (Standard), oder nur eins von beiden.

## Datenschutz

- Keine Analyse-Dienste, keine Werbung.
- Persönliche Angaben (Gewicht, Gesundheitswerte, Journal) nur in Nutzerdaten, nie in diesem Repository.
- Externe Dienste: GitHub (Sync, verschlüsselt), ntfy.sh (Erinnerungstexte, nur wenn eingeschaltet).
