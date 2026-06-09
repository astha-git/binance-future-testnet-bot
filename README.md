
# Binance Futures Testnet Trading Bot

## Overview
A Python-based CLI trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).  
The project demonstrates API integration, input validation, structured logging, and error handling.


## Features
- Place MARKET orders
- Place LIMIT orders
- BUY / SELL support
- Input validation (symbol, side, type, quantity, price)
- Structured logging of requests and responses
- Exception handling for API and network errors

## Project Structure

trading_bot/
│
├── bot/
│   ├── **init**.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   └── exceptions.py
│
├── logs/
├── cli.py
├── requirements.txt
├── .env
└── README.md

## Setup Instructions

### 1. Clone Repository

  bash
git clone https://github.com/astha-git/binance-future-testnet-bot.git
cd binance-future-testnet-bot


### 2. Create Virtual Environment (Optional but Recommended)

   bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # Mac/Linux

### 3. Install Dependencies

  bash
pip install -r requirements.txt


### 4. Create `.env` File

Create a file named `.env` in the root directory:

  env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret

### 5. Get Binance Testnet API Keys

* Visit: [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
* Create account or login
* Generate API Key & Secret
* Add them to `.env`

## Usage

### MARKET Order Example

  bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT Order Example

 bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000

## CLI Arguments

| Argument | Required   | Description                  |
| -------- | ---------- | ---------------------------- |
| symbol   | Yes        | Trading pair (e.g., BTCUSDT) |
| side     | Yes        | BUY or SELL                  |
| type     | Yes        | MARKET or LIMIT              |
| quantity | Yes        | Order quantity               |
| price    | Only LIMIT | Limit order price            |

## Example Output

===== ORDER SUMMARY =====
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

===== RESPONSE =====
Order ID: 123456789
Status: NEW
Executed Qty: 0.001
Average Price: 65000.0

Order placed successfully

## Logging

Logs are stored in:

logs/trading_bot.log




Just tell me 👍
```
