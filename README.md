# 🧠 GPT Crypto Intelligence API

A powerful FastAPI backend built for **OpenAI GPT Actions**, enabling advanced multi-chain crypto analysis.  
Supports wallet lookups, smart contract verification, price tracking, news aggregation and historical chart data.

## 🚀 Features

- 📊 Real-time price data via CoinGecko  
- 📰 Latest crypto news via NewsAPI  
- 🧾 Wallet balance fetch for:
  - Ethereum (via Etherscan)
  - Base (via BaseScan)
  - Solana (via Solscan)
  - Bitcoin (via Blockstream)
  - XRP (via XRPL Data API)  
- 📜 Smart contract source + compiler info (via Etherscan)  
- 📈 Historical price charts  
- 🔐 `.env` support for secure API key handling  
- 🌐 Fully deployable on Render or any cloud platform  

## ⚙️ Requirements

- Python 3.10+  
- API Keys:
  - `NEWS_API_KEY` (https://newsapi.org)
  - `ETHERSCAN_API_KEY` (https://etherscan.io)
  - `BASESCAN_API_KEY` (https://basescan.org)

## 🛠️ Local Setup

1. Clone the repo  
2. Create `.env` from `.env.example` and insert your keys  
3. Run:
   - `pip install -r requirements.txt`
   - `uvicorn main:app --reload`  
4. Server runs at: `http://127.0.0.1:8000`

## 🌐 Deploy on Render

1. Go to [https://render.com](https://render.com)  
2. Create new **Web Service**  
3. Connect your GitHub repo  
4. Set:
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port 10000`
   - Port: `10000`  
   - Environment Variables:
     - `NEWS_API_KEY`
     - `ETHERSCAN_API_KEY`
     - `BASESCAN_API_KEY`

## 🤖 Use with GPT Actions

1. Go to [https://chat.openai.com/gpts](https://chat.openai.com/gpts)  
2. Edit your GPT  
3. Go to **Actions → Upload File**  
4. Upload `crypto_api_action.json`  
5. Update `"servers"` URL to your Render domain

## 🔎 Example API Endpoints

- `/wallet_info?address=0x...`
- `/wallet_info_base?address=0x...`
- `/wallet_info_solana?address=...`
- `/wallet_info_btc?address=...`
- `/wallet_info_xrp?address=...`
- `/get_price?coin=bitcoin&currency=usd`
- `/get_news?coin=solana`
- `/historical_price?coin=ethereum&days=30`
- `/contract_info?address=0x...`

## 📄 License

MIT License  
© [ghiemer](https://github.com/ghiemer)
