import nltk
# nltk.download('punkt_tab')

import requests
import random
import nltk
from nltk.tokenize import word_tokenize

# Initialize NLTK tokenizer
# nltk.download('punkt')

# CoinGecko API endpoint for simple price and market data
def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": "bitcoin,ethereum,cardano",
        "order": "market_cap_desc"
    }
    response = requests.get(url, params=params)
    data = response.json()
    crypto_data = {}
    for coin in data:
        crypto_data[coin['name']] = {
            "price": coin['current_price'],
            "price_trend": "rising" if coin['price_change_percentage_24h'] > 0 else "falling",
            "market_cap": "high" if coin['market_cap_rank'] <= 3 else "medium"
        }
    return crypto_data

# Add static sustainability scores (as API doesn’t provide this)
sustainability_scores = {
    "Bitcoin": 3/10,
    "Ethereum": 6/10,
    "Cardano": 8/10
}

greetings = [
    "Hey there! Let's find you a green and growing crypto!",
    "Welcome to CryptoAdvisor! Ready to explore sustainable investments?",
    "Hello crypto enthusiast! Let's analyze some profitable and eco-friendly options."
]

def chatbot_response(user_query, crypto_db):
    tokens = word_tokenize(user_query.lower())

    if any(word in tokens for word in ["hi", "hello", "hey"]):
        return random.choice(greetings)

    if any(word in user_query for word in ["sustainable", "eco", "green"]):
        recommend = max(crypto_db, key=lambda x: sustainability_scores.get(x, 0))
        return f"Invest in {recommend}! It’s eco-friendly and has long-term potential!"

    elif any(word in user_query for word in ["trending", "rising", "trend"]):
        trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"The trending cryptos are: {', '.join(trending)}!"

    elif any(word in user_query for word in ["long-term", "growth", "hold"]):
        for name in crypto_db:
            if crypto_db[name]["price_trend"] == "rising" and sustainability_scores.get(name, 0) > 0.7:
                return f" {name} is trending up and has a top-tier sustainability score!"

    elif any(word in user_query for word in ["profitable", "make money", "best return"]):
        for name in crypto_db:
            if crypto_db[name]["price_trend"] == "rising" and crypto_db[name]["market_cap"] == "high":
                return f"{name} looks profitable with a rising trend and high market cap!"

    elif any(word in user_query for word in ["safe", "recommend", "buy"]):
        good_choices = [name for name in crypto_db
                        if crypto_db[name]["price_trend"] == "rising" and sustainability_scores.get(name, 0) > 0.6]
        if good_choices:
            return f"Consider investing in: {', '.join(good_choices)} based on current trends and sustainability."
        else:
            return "❓ I couldn't find a solid recommendation right now. Try again later."

    elif any(word in user_query for word in ["disclaimer", "risk"]):
        return "⚠️ Crypto is risky—always do your own research before investing."

    else:
        return "Hmm, I’m not sure about that. Try asking about sustainability, trends, or long-term growth!"

# Start chatbot
print("👋 Hey there! I’m CryptoBuddy, your friendly crypto guide! Let's find you a green and growing crypto! 🚀🌱")
print("Type 'exit' to end the chat.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("CryptoBuddy: Bye! Remember—crypto is risky. Do your own research!")
        break
    try:
        live_crypto_data = fetch_crypto_data()
        # Merge with sustainability scores
        for name in live_crypto_data:
            live_crypto_data[name]["sustainability_score"] = sustainability_scores.get(name, 0)
        response = chatbot_response(user_input, live_crypto_data)
    except Exception as e:
        response = f"⚠️ Sorry, I couldn't fetch live data right now. Try again later. ({e})"
    print("CryptoBuddy:", response)
