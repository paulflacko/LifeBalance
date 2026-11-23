# 07 · Hantelwoche auf dem Handy starten, ohne Claude zu öffnen

Es gibt drei Wege. Sie unterscheiden sich vor allem darin, wo deine Einträge gespeichert werden.

| Weg | Was du brauchst | Wo die Daten liegen | Offline |
| --- | --- | --- | --- |
| **1. Link im Handy-Browser** | Anmeldung bei claude.ai im Browser | im Claude-Konto, auf Handy und Laptop gleich | nein |
| **2. Eigene Adresse (Handy-App)** | einmal den Ordner `handy-app/` hochladen | nur auf dem Handy (Sicherung als Datei möglich) | ja |
| **3. Offline-Datei** | Datei `hantelwoche-offline.html` | nur in diesem Browser | ja, aber am Handy umständlich |

## 1. Link im Handy-Browser

1. Den App-Link in Safari (iPhone) oder Chrome (Android) öffnen, nicht in der Claude-App. Falls sich die Claude-App öffnet: Link lange drücken und „In Safari öffnen“ bzw. „In Chrome öffnen“ wählen.
2. Einmal bei claude.ai anmelden.
3. iPhone: Teilen-Symbol › „Zum Home-Bildschirm“. Android: Menü ⋮ › „Zum Startbildschirm hinzufügen“.

Danach startet Hantelwoche vom Startbildschirm, ohne dass du die Claude-App öffnest. Die Daten bleiben im Konto und sind auch am Laptop da.

## 2. Eigene Adresse (echte Handy-App, auch offline)

Der Ordner `handy-app/` (bzw. `hantelwoche-handy-app.zip`) ist eine fertige installierbare Web-App mit eigenem Symbol. Sie läuft nach dem ersten Öffnen auch ohne Internet. Sie braucht nur eine Adresse im Internet:

- **Netlify Drop:** app.netlify.com/drop öffnen, kostenloses Konto anlegen, den Ordner `handy-app` in das Fenster ziehen. Du bekommst eine Adresse wie `https://hantelwoche-xyz.netlify.app`.
- **GitHub Pages (gewählt):** Die App liegt im Repository `paulflacko/Hantelwoche-v1`. Einmalig in GitHub unter Settings › Pages bei „Source“ „Deploy from a branch“, Branch `main`, Ordner `/ (root)` wählen und speichern. Adresse danach: `https://paulflacko.github.io/Hantelwoche-v1/`. Bei einem privaten Repository geht Pages nur mit GitHub Pro; sonst das Repository auf öffentlich stellen (es enthält nur den App-Code, keine Trainingsdaten).

Die Adresse am Handy öffnen und wie oben „Zum Startbildschirm“ wählen.

**Wichtig:** Diese Version speichert nur auf dem Handy, nicht im Claude-Konto. Um Daten mitzunehmen, in der Artifact-Version unter Einstellungen „Daten als Datei sichern“ wählen und in der Handy-App „Sicherung laden“. Nach Änderungen an der App muss der Ordner neu hochgeladen werden (`python3 build_pwa.py`).

## 3. Offline-Datei

`hantelwoche-offline.html` läuft per Doppelklick am Laptop. Am Handy lässt sich eine lokale HTML-Datei je nach Browser nur umständlich oder gar nicht öffnen. Für das Handy ist deshalb Weg 1 oder 2 besser.

## Online speichern mit GitHub, verschlüsselt (ab 03.11.2026)

Die Handy-App speichert alle Einträge automatisch als `data.json` im Zweig `daten` des Repositorys `paulflacko/Hantelwoche-v1`. Die Datei ist mit AES-GCM 256 verschlüsselt. Der Schlüssel entsteht aus einem Passwort (PBKDF2-SHA256, 310 000 Runden), das nur auf deinen Geräten liegt. Auf GitHub steht nur unlesbarer Zeichensalat, obwohl das Repository öffentlich ist.

1. Token erstellen: github.com › Settings › Developer settings › Personal access tokens › Fine-grained tokens › Generate new token. Repository access: „Only select repositories“ › `Hantelwoche-v1`. Permissions › Repository permissions › Contents: „Read and write“. Ablaufdatum z. B. 1 Jahr.
2. In der Handy-App: Einstellungen › „Online speichern mit GitHub“ › Token und ein Passwort (mind. 8 Zeichen) eintragen › Verbinden. Auf jedem weiteren Gerät dasselbe Passwort verwenden.
3. Bisherige Daten aus der Claude-Version: vorher einmal „Sicherung laden“ mit `sicherung/hantelwoche-sicherung-2026-11-03.json`.

Die App gleicht beim Start, beim Zurückkehren in die App und wenige Sekunden nach jeder Änderung ab. Pro Eintrag (Tag, Einheit, Profil) gewinnt der neuere Stand. **Passwort vergessen = Online-Daten verloren** (die Kopie auf dem Gerät bleibt). Die Offline-Datei kann nicht verschlüsseln, weil Browser das nur über https erlauben.
