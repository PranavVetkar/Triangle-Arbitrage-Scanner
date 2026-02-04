# 🔺 Triangular Arbitrage Scanner (Crypto)

A Python-based **triangular arbitrage scanner** that detects pricing inefficiencies **within a single exchange** by cycling capital across three trading pairs.

This project demonstrates how small price mismatches between correlated markets can create **short-lived arbitrage opportunities**.

---

## 🚀 What This Project Does

- Connects to **Binance** using CCXT
- Monitors three related trading pairs:
  - `BTC/USDT`
  - `ETH/BTC`
  - `ETH/USDT`
- Simulates a **triangular trade loop**
- Calculates net profit or loss per cycle
- Continuously scans the market in real time

---

## 🧠 Triangular Arbitrage Logic

The strategy follows this loop:
- USDT → BTC → ETH → USDT

### Step-by-step:
1. Convert **USDT → BTC** using `BTC/USDT`
2. Convert **BTC → ETH** using `ETH/BTC`
3. Convert **ETH → USDT** using `ETH/USDT`
4. Compare final USDT with initial amount

If the final amount is greater, an arbitrage opportunity exists.

---

## 🧮 Profit Calculation
- Profit = Final USDT − Initial USDT
- Profit % = (Profit / Initial USDT) × 100

The script flags:
- ✅ **PROFIT** loops
- ❌ **LOSS** loops

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **CCXT**
- **Binance REST API**
- **Time-based polling**

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/PranavVetkar/Triangle-Arbitrage-Scanner.git
cd Triangle-Arbitrage-Scanner

