# 🧠 old btc Wallet 

A high-performance CLI tool to **fetch top Bitcoin wallet addresses** and **check their balances concurrently** using multi-threading.

---

## 🚀 Features

- 🔍 Fetch top BTC addresses from [BitInfoCharts](https://bitinfocharts.com/)
- ⚡ Multi-threaded balance checking (ultra-fast)
- 🎯 Filter results by minimum BTC balance
- 🧾 Outputs to terminal **and** structured `results.json` file
- 💡 Lightweight, easy-to-use CLI tool

---

## 🧰 Requirements

- Python 3.7+
- `pip` (Python package manager)

📥 Clone the repo:
```bash
git clone https://github.com/PARSAJF807/oldbtcwallet.git
cd oldbtcwallet
```

ℹ️Install dependencies:

```bash
pip install -r requirements.txt
```

---

⚙️ Usage
```
python main.py --top 500 --min-btc 10 --threads 50 
```

CLI Parameters:

Argument	Description	Default

--top	Number of top BTC addresses to fetch	100
--min-btc	Minimum BTC balance required to include in result	1.0
--threads	Number of threads to use for balance checking	20



---

📂 Output

After execution:

✅ Shows results in terminal

✅ Saves structured data to results.json

```
Example:

[
  {
    "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
    "balance_btc": 104.2998
  },
  {
    "address": "1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF",
    "balance_btc": 79957.268
  }
]
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) — feel free to use, modify, and distribute it.

---

👨‍💻 Author
 Made by [PARSAJF807](https://github.com/PARSAJF807)
