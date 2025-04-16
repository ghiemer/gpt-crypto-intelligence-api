# 🧠 GPT Crypto Intelligence API

Ein leistungsstarkes FastAPI-Backend für **OpenAI GPT Actions**, das mehrere Blockchains unterstützt.  
Mit diesem Projekt kannst du Kryptowährungen analysieren, Wallets prüfen, Smart Contracts inspizieren, Kursverläufe abrufen und News anzeigen – alles gesteuert durch deinen GPT.

---

## 🚀 Features

- 📊 Preisabfragen über CoinGecko
- 📰 Krypto-News über NewsAPI
- 🧾 Wallet-Analyse für:
  - Ethereum (Etherscan)
  - Base (BaseScan)
  - Solana (Solscan)
  - Bitcoin (Blockstream)
  - XRP (XRPL Data API)
- 📜 Smart Contract Verifikation (Etherscan)
- 📈 Historische Kursdaten (CoinGecko)
- 🔐 API-Key Handling via `.env`
- 🌐 Bereit für Deployment auf Render

---

## ⚙️ Voraussetzungen

- Python 3.10 oder höher
- API Keys:
  - `NEWS_API_KEY` (https://newsapi.org)
  - `ETHERSCAN_API_KEY` (https://etherscan.io)
  - `BASESCAN_API_KEY` (https://basescan.org)

---

## 🛠️ Lokale Installation

```bash
git clone https://github.com/ghiemer/gpt-crypto-intelligence-api.git
cd gpt-crypto-intelligence-api

# (optional) virtuelle Umgebung aktivieren
python -m venv venv
source venv/bin/activate

# Abhängigkeiten installieren
pip install -r requirements.txt

# .env Datei erstellen und Keys einfügen
cp .env.example .env

# Server starten
uvicorn main:app --reload
```

→ Jetzt erreichbar unter: http://127.0.0.1:8000

---

## 🌐 Deployment mit Render (kostenlos)

1. Gehe auf https://render.com
2. Neues Web Service erstellen
3. Verbinde dein GitHub-Repo
4. Konfiguration:
   - **Start Command**:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 10000
     ```
   - **Port:** `10000`
   - **Environment Variables**:
     - `NEWS_API_KEY`
     - `ETHERSCAN_API_KEY`
     - `BASESCAN_API_KEY`

---

## 🤖 Integration mit GPT Actions

1. Gehe zu: https://chat.openai.com/gpts
2. Öffne deinen Custom GPT
3. Gehe zu **Actions** → „Upload File“
4. Lade `crypto_api_action.json` hoch
5. Passe darin die URL an:
   ```json
   "servers": [
     { "url": "https://dein-service.onrender.com" }
   ]
   ```

---

## 🔎 Beispiel-API-Requests

```http
GET /wallet_info?address=0x...
GET /wallet_info_base?address=0x...
GET /wallet_info_solana?address=...
GET /wallet_info_btc?address=...
GET /wallet_info_xrp?address=...

GET /get_price?coin=solana&currency=eur
GET /get_news?coin=bitcoin
GET /historical_price?coin=ethereum&days=7
GET /contract_info?address=0x...
```

---

## 🧪 Testmöglichkeiten

Rufe z. B. direkt `https://dein-service.onrender.com/get_price?coin=bitcoin&currency=eur` im Browser oder Postman auf, um zu prüfen, ob dein Server korrekt läuft.

---

## 📄 Lizenz

MIT License  
© [ghiemer](https://github.com/ghiemer)

---

## 🙋 Support

Bei Fragen, Ideen oder Erweiterungswünschen einfach im Repo ein Issue eröffnen – oder melde dich direkt.
