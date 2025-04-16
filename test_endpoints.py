import requests

BASE_URL = "http://127.0.0.1:8000"

# ✅ Testcases: (coin, currency)
def test_get_price():
    response = requests.get(f"{BASE_URL}/get_price?coin=bitcoin&currency=eur")
    assert response.status_code == 200
    print("✅ get_price passed:", response.json())

def test_get_news():
    response = requests.get(f"{BASE_URL}/get_news?coin=ethereum")
    assert response.status_code == 200
    print("✅ get_news passed:", response.json())

def test_wallet_eth():
    response = requests.get(f"{BASE_URL}/wallet_info?address=0x000000000000000000000000000000000000dead")
    assert response.status_code == 200
    print("✅ ETH wallet passed:", response.json())

def test_wallet_base():
    response = requests.get(f"{BASE_URL}/wallet_info_base?address=0x000000000000000000000000000000000000dead")
    assert response.status_code == 200
    print("✅ Base wallet passed:", response.json())

def test_wallet_bsc():
    response = requests.get(f"{BASE_URL}/wallet_info_bsc?address=0x000000000000000000000000000000000000dead")
    assert response.status_code == 200
    print("✅ BSC wallet passed:", response.json())

def test_wallet_btc():
    response = requests.get(f"{BASE_URL}/wallet_info_btc?address=bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh")
    assert response.status_code == 200
    print("✅ BTC wallet passed:", response.json())

def test_wallet_solana():
    response = requests.get(f"{BASE_URL}/wallet_info_solana?address=FjACX31LP3zk4TTSYq6LSzvRQ2R5nKYnrKhSg6VjYDz8")
    assert response.status_code == 200
    print("✅ Solana wallet passed:", response.json())

def test_wallet_xrp():
    response = requests.get(f"{BASE_URL}/wallet_info_xrp?address=rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv")
    assert response.status_code == 200
    print("✅ XRP wallet passed:", response.json())

def test_contract_info():
    response = requests.get(f"{BASE_URL}/contract_info?address=0xdAC17F958D2ee523a2206206994597C13D831ec7")
    assert response.status_code == 200
    print("✅ Contract info passed:", response.json())

def test_historical_price():
    response = requests.get(f"{BASE_URL}/historical_price?coin=ethereum&currency=eur&days=7")
    assert response.status_code == 200
    print("✅ Historical price passed:", response.json())

if __name__ == "__main__":
    test_get_price()
    test_get_news()
    test_wallet_eth()
    test_wallet_base()
    test_wallet_bsc()
    test_wallet_btc()
    test_wallet_solana()
    test_wallet_xrp()
    test_contract_info()
    test_historical_price()
