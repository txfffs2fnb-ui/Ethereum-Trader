# Ethereum Trader Bot (FreqAI)

Dieses Repository enthält eine KI-basierte Trading-Konfiguration für Ethereum unter Nutzung von **Freqtrade**, **Docker** und **FreqAI**.

## Algorithmus & Modelle

Das System nutzt nun den **FreqAI** Algorithmus zur Preisvorhersage.
*   **Modell:** Nutzt Machine Learning (z.B. XGBoost via FreqAI), um Preisänderungen für die nächsten 2 Stunden (24 Candles à 5m) vorherzusagen.
*   **Strategie:** `EthereumFreqaiStrategy` verwendet technische Indikatoren (RSI, MFI, ADX) als Features für das Modell.
*   **GitHub Models:** Die Integration von GitHub Models (Preview) ist im Repository aktiviert, um Modell-Experimente zu verfolgen.

## Voraussetzungen

* [Docker Desktop](https://www.docker.com/products/docker-desktop) installiert

## Schnelleinrichtung

1. Klone dieses Repository.
2. Initialisiere die Ordnerstruktur:
   ```bash
   docker compose run --rm freqtrade create-userdir --userdir user_data
   ```
3. Starte das Training und den Bot:
   ```bash
   docker compose up -d
   ```
4. Web-Interface: `http://localhost:8080` (admin/password)

## Training & Backtesting

Um das Modell mit historischen Ethereum-Daten zu trainieren und zu testen:

1. Daten laden:
   ```bash
   docker compose run --rm freqtrade download-data --pairs ETH/USDT --exchange binance -t 5m
   ```
2. Backtesting (inkl. Training):
   ```bash
   docker compose run --rm freqtrade backtesting --strategy EthereumFreqaiStrategy --config config.json --freqaimodel LightGBMRegressor --timerange 20240101-
   ```

**Hinweis:** Das erste Training kann je nach Hardware einige Minuten dauern. FreqAI speichert die Modelle im Ordner `user_data/models`.
