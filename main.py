from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import requests
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# CORS setup to allow calls from GPT
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chat.openai.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load API keys from environment
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
BASESCAN_API_KEY = os.getenv("BASESCAN_API_KEY")

# Global error handler
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"error": "An unexpected error occurred."}
    )

# Get current crypto price from CoinGecko
@app.get("/get_price")
def get_price(coin: str, currency: str):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if coin not in data:
            raise HTTPException(status_code=404, detail="Coin not found.")
        return data
    except Exception as e:
        logger.error(f"Price fetch error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch price")

# Get news articles for a cryptocurrency using NewsAPI
@app.get("/get_news")
def get_news(coin: str):
    try:
        if not NEWS_API_KEY:
            raise HTTPException(status_code=500, detail="NEWS_API_KEY missing.")
        url = f"https://newsapi.org/v2/everything?q={coin}&sortBy=publishedAt&language=en&pageSize=5&apiKey={NEWS_API_KEY}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        if not articles:
            return {"message": "No news found."}
        return [
            {
                "title": a["title"],
                "url": a["url"],
                "source": a["source"]["name"],
                "publishedAt": a["publishedAt"]
            }
            for a in articles
        ]
    except Exception as e:
        logger.error(f"News fetch error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch news")

# Get Ethereum wallet balance using Etherscan API
@app.get("/wallet_info")
def wallet_info(address: str):
    try:
        url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={ETHERSCAN_API_KEY}"
        res = requests.get(url, timeout=10)
        data = res.json()
        balance = int(data["result"]) / 1e18
        return {"address": address, "eth_balance": balance}
    except Exception as e:
        logger.error(f"ETH Wallet error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch ETH wallet info")

# Get Base wallet balance using BaseScan API
@app.get("/wallet_info_base")
def wallet_info_base(address: str):
    try:
        url = f"https://api.basescan.org/api?module=account&action=balance&address={address}&tag=latest&apikey={BASESCAN_API_KEY}"
        res = requests.get(url, timeout=10)
        data = res.json()
        balance = int(data["result"]) / 1e18
        return {"address": address, "base_balance": balance}
    except Exception as e:
        logger.error(f"Base Wallet error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch Base wallet info")

# Get Solana wallet balance using Solscan public API
@app.get("/wallet_info_solana")
def wallet_info_solana(address: str):
    try:
        url = f"https://public-api.solscan.io/account/{address}"
        headers = {"accept": "application/json"}
        res = requests.get(url, headers=headers, timeout=10)
        data = res.json()
        sol_balance = data.get("lamports", 0) / 1e9
        return {"address": address, "sol_balance": sol_balance}
    except Exception as e:
        logger.error(f"Solana Wallet error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch Solana wallet info")

# Get Bitcoin wallet balance using Blockstream API
@app.get("/wallet_info_btc")
def wallet_info_btc(address: str):
    try:
        url = f"https://blockstream.info/api/address/{address}"
        res = requests.get(url, timeout=10)
        data = res.json()
        balance = data.get("chain_stats", {}).get("funded_txo_sum", 0) / 1e8
        return {"address": address, "btc_balance": balance}
    except Exception as e:
        logger.error(f"Bitcoin Wallet error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch BTC wallet info")

# Get XRP wallet balance using Ripple public API
@app.get("/wallet_info_xrp")
def wallet_info_xrp(address: str):
    try:
        url = f"https://data.ripple.com/v2/accounts/{address}/balances"
        res = requests.get(url, timeout=10)
        balances = res.json().get("balances", [])
        xrp_balance = next((b["value"] for b in balances if b["currency"] == "XRP"), "0")
        return {"address": address, "xrp_balance": float(xrp_balance)}
    except Exception as e:
        logger.error(f"XRP Wallet error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch XRP wallet info")

# Get smart contract info (verification status, compiler version) from Etherscan
@app.get("/contract_info")
def contract_info(address: str):
    try:
        url = f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={address}&apikey={ETHERSCAN_API_KEY}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json().get("result", [])[0]
        if not data or not data["SourceCode"]:
            return {"verified": False, "message": "Contract is not verified"}
        return {
            "verified": True,
            "contractName": data["ContractName"],
            "compilerVersion": data["CompilerVersion"],
            "sourceCode": data["SourceCode"][:300] + "...",
        }
    except Exception as e:
        logger.error(f"Contract info error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch contract info")

# Get historical price chart for a coin from CoinGecko
@app.get("/historical_price")
def historical_price(coin: str, currency: str = "eur", days: int = 7):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart?vs_currency={currency}&days={days}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        prices = [{"timestamp": ts, "price": price} for ts, price in data.get("prices", [])]
        return {"coin": coin, "currency": currency, "days": days, "prices": prices}
    except Exception as e:
        logger.error(f"Historical price error: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch historical price")
