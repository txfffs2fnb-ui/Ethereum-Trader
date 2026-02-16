# Ethereum Trader Bot (Freqtrade)

Dieses Repository enthält die Konfiguration für einen Ethereum-basierten Trading-Bot unter Nutzung von **Freqtrade** und **Docker**.

## Voraussetzungen

* [Docker Desktop](https://www.docker.com/products/docker-desktop) installiert

## Schnelleinrichtung

1. Klone dieses Repository auf deinen Computer.
2. Öffne ein Terminal im Repository-Ordner.
3. Führe diesen Befehl aus, um die Ordnerstruktur zu erstellen:
   ```bash
   docker compose run --rm freqtrade create-userdir --userdir user_data
   ```
4. Starte den Bot (Dry-Run Modus standardmäßig):
   ```bash
   docker compose up -d
   ```
5. Greife auf das Web-Interface zu: `http://localhost:8080` (Nutzer: admin, Passwort: password)

## Ethereum Backtesting

Um die Performance mit Ethereum-Daten zu testen:

1. Kursdaten herunterladen:
   ```bash
   docker compose run --rm freqtrade download-data --pairs ETH/USDT --exchange binance -t 5m 1h
   ```
2. Backtest starten:
   ```bash
   docker compose run --rm freqtrade backtesting --strategy SampleStrategy --timerange 20240101-
   ```

**Hinweis:** Die Strategie `SampleStrategy` ist ein Platzhalter. Du kannst eigene Strategien im Ordner `user_data/strategies` hinzufügen.
