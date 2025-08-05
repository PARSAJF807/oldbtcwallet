import requests
from bs4 import BeautifulSoup

def fetch_top_addresses(n=500):
    url = "https://bitinfocharts.com/top-100-richest-bitcoin-addresses.html"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    rows = soup.select("table.table-striped tbody tr")[:n]
    out = []
    for tr in rows:
        addr = ''.join(tr.select_one("td:nth-child(2) a:not([style])").text.strip().split())
        balance = tr.select_one("td:nth-child(3)").text.strip().split(" ")[0]
        out.append((addr, float(balance)))
    return out
