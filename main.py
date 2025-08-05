import argparse, json
from fetch_addresses import fetch_top_addresses
from check_balance import batch_check

def main():
    parser = argparse.ArgumentParser(description="BTC address analyzer CLI")
    parser.add_argument("--top", type=int, default=100, help="how many top addresses")
    parser.add_argument("--min-btc", type=float, default=1.0, help="min BTC to include")
    parser.add_argument("--threads", type=int, default=20, help="number of threads")
    args = parser.parse_args()

    print(f"☎️ Fetching top {args.top} addresses…")
    addrs = fetch_top_addresses(args.top)
    print(f"📊 Checking balances with {args.threads} threads…")
    res = batch_check(addrs, threads=args.threads)
    filtered = [r for r in res if r["balance_btc"] and r["balance_btc"] >= args.min_btc]

    print(f"🎯 Found {len(filtered)} addresses ≥ {args.min_btc} BTC")
    for r in filtered[:10]:
        print(f"{r['address']}: {r['balance_btc']} BTC")

    with open("results.json", "w") as f:
        json.dump(filtered, f, indent=2)
    print("💾 Results saved to results.json")

if __name__ == "__main__":
    main()
