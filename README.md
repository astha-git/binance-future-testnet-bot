# Binance Futures Testnet Trading Bot

## Overview
A Python CLI-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

## Features
- Place MARKET orders
- Place LIMIT orders
- BUY / SELL support
- Input validation
- Structured logging
- Error handling for API and network issues

---

## Project Structure

trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── exceptions.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
├── cli.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
