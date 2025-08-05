import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

API_URL = "https://blockstream.info/api/address/{addr}"

def get_balance(addr):
    try:
        r = requests.get(API_URL.format(addr=addr), timeout=10)
        r.raise_for_status()
        data = r.json()
        stats = data.get("chain_stats", {})
        sats = stats.get("funded_txo_sum",0) - stats.get("spent_txo_sum",0)
        return addr, sats / 1e8
    except Exception as e:
        return addr, None

def batch_check(addresses, threads=10):
    results = []
    with ThreadPoolExecutor(max_workers=threads) as ex:
        futures = {ex.submit(get_balance, addr): addr for addr,_ in addresses}
        for f in as_completed(futures):
            addr, bal = f.result()
            results.append({"address": addr, "balance_btc": bal})
    return results
