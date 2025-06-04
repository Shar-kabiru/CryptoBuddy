# 🧠 CryptoBuddy – A Rule-Based Crypto Investment Chatbot

CryptoBuddy is a Python chatbot that provides basic cryptocurrency investment advice with a focus on **profitability** and **sustainability**. It mimics simple AI decision-making by using rule-based logic and optional natural language processing (NLP).

---

## 🚀 Features

- 💬 Responds to user queries using predefined rules.
- 🌱 Recommends eco-friendly and long-term investment options.
- 📈 Identifies trending and profitable cryptocurrencies.
- 🔗 Integrates with the **CoinGecko API** to fetch **real-time market data** (in `CryptoChat.py`).
- 🧠 Uses **NLTK** for better understanding of user input (in `CryptoChat.py`).

---

## 🗂 File Overview

| File           | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `chat.py`      | Basic rule-based chatbot without API or NLP. Uses static data.              |
| `CryptoChat.py`| Advanced version with CoinGecko API and NLTK integration for NLP.           |

---

## 🔧 Requirements

- `requests` for API calls
- `nltk` for natural language processing (in `CryptoChat.py`)

### Install Dependencies
  pip install requests nltk

### Download NLTK Data (once only)
    import nltk
    nltk.download('punkt')

## Example Queries

Which coin is the most profitable?

Recommend a green investment

What crypto is trending?

Is it safe to invest in Cardano?

Hello

**⚠️ Disclaimer**

This chatbot is for educational purposes only. It does not provide financial advice. Always do your own research before investing in cryptocurrencies.
