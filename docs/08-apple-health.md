# 08 · Apple Health und Apple Watch

LifeBalance ist zunächst eine Web-App (siehe [Technik](09-technik.md)). Web-Apps laufen nicht auf der Uhr, und Apple Health ist für Websites nicht direkt lesbar. Deshalb drei Stufen:

## Stufe 1: Kurzbefehl-Import (empfohlen, zuerst)

Ein iPhone-Kurzbefehl liest morgens aus Health:

- Schlafdauer der letzten Nacht
- Ruhepuls
- HRV (Herzfrequenzvariabilität)
- Schritte von gestern

und öffnet LifeBalance mit diesen Werten in der Adresse, z. B. `…/#import?schlaf=7.2&ruhepuls=54&hrv=48&schritte=8400&datum=2026-11-23`. Die App speichert sie als Einträge mit `quelle: health` und füllt den Check-in vor. Kein Umbau der Plattform, kostenlos. Der Kurzbefehl lässt sich per Automation täglich um 7 Uhr auslösen.

Die App liefert eine Anleitung und einen Link zum fertigen Kurzbefehl.

## Stufe 2: Training mit der Uhr

Die Uhr misst Training in der Workout-App mit. Ein zweiter Kurzbefehl holt Dauer, Durchschnittspuls und Kalorien des letzten Workouts und ordnet sie der Einheit des Tages zu.

## Stufe 3: Eigene native App

Eine echte iOS- und Watch-App (Swift) könnte Health direkt lesen und auf der Uhr Sätze zählen. Großer Schritt, Apple-Entwicklerkonto nötig. Erst sinnvoll, wenn LifeBalance im Alltag sitzt.

## Erinnerungen auf der Uhr

Laufen schon heute über ntfy: In der Watch-App auf dem iPhone › Mitteilungen › ntfy › „iPhone spiegeln“ ([Erinnerungen](07-erinnerungen.md)).
