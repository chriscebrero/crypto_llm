import requests
from datetime import datetime

BASE_URL = "https://api.coingecko.com/api/v3"

def get_crypto_data(symbol):
    """
    Fetches the current cryptocurrency data for the given symbol using the CoinGecko API.
    
    Args:
        symbol (str): Cryptocurrency symbol (e.g., "bitcoin").
        
    Returns:
        list: List of tuples containing cryptocurrency data for the last few days, sorted by most recent date.
    """
    # This is the API endpoint to get market data for the past few days
    response = requests.get(f"{BASE_URL}/coins/{symbol}/market_chart", params={"vs_currency": "usd", "days": "5"})
    
    if response.status_code == 200:
        data = response.json()
        # Extract prices, each data point includes [timestamp, price]
        price_data = data.get("prices", [])
        # Format the data as a list of tuples (date, price) with the date in descending order
        formatted_data = []
        for entry in price_data:
            timestamp, price = entry
            date = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')  # Convert timestamp to date string
            if not any(d == date for d, _ in formatted_data):  # Avoid duplicate dates
                formatted_data.append((date, {"Price": price}))

        # Sort formatted_data by date in descending order
        sorted_data = sorted(formatted_data, key=lambda x: x[0], reverse=True)
        print(sorted_data)
        return sorted_data
    else:
        print("Failed to retrieve data from CoinGecko API.")
        return []
