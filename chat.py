# CryptoBuddy - A Rule-Based Crypto Investment Chatbot

import random

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

greetings = [
    "Hey there! Let's find you a green and growing crypto!",
    "Welcome to CryptoAdvisor! Ready to explore sustainable investments?",
    "Hello crypto enthusiast! Let's analyze some profitable and eco-friendly options."
]

def chatbot_response(user_query):
    user_query = user_query.lower()
    words = user_query.split()


    if any(greet in words for greet in ["hi", "hello", "hey"]):
        return random.choice(greetings)

    if "sustainable" in user_query or "eco" in user_query or "most green" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"\U0001F331 Invest in {recommend}! It’s eco-friendly and has long-term potential!"

    elif "trending" in user_query or "rising" in user_query or "trends" in user_query:
        trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"\U0001F4C8 The trending cryptos are: {', '.join(trending)}!"

    elif "long-term" in user_query or "growth" in user_query or "hold" in user_query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                return f"\U0001F680 {name} is trending up and has a top-tier sustainability score!"

    elif "profitable" in user_query or "make money" in user_query or "best return" in user_query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                return f"\U0001F4B0 {name} looks profitable with a rising trend and high market cap!"

    elif "safe" in user_query or "recommend" in user_query or "which should i buy" in user_query:
        good_choices = [name for name, data in crypto_db.items()
                        if data["price_trend"] == "rising" and data["sustainability_score"] > 0.6]
        if good_choices:
            return f"\U0001F4A1 Consider investing in: {', '.join(good_choices)} based on current trends and sustainability."
        else:
            return "❓ I couldn't find a solid recommendation right now. Try again later."

    elif "disclaimer" in user_query or "risk" in user_query:
        return "⚠️ Crypto is risky—always do your own research before investing."

    else:
        return "\U0001F916 Hmm, I’m not sure about that. Try asking about sustainability, trends, or long-term growth!"

print("👋 Hey there! I’m CryptoBuddy, your friendly crypto guide! Let's find you a green and growing crypto! 🚀🌱")
print("Type 'exit' to end the chat.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("CryptoBuddy: Bye! Remember—crypto is risky. Do your own research! \U0001F44B")
        break
    response = chatbot_response(user_input)
    print("CryptoBuddy:", response)
