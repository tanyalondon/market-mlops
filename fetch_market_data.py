import os
import requests
import pandas as pd
import yfinance as yf
from dotenv import load_dotenv
load_dotenv()

MY_KEY = os.getenv('ALPHAVANTAGE_API_KEY')

SYMBOL = 'NVDA' 

# This is a solid, pre-built link. Do not change anything but the API key at the end.
URL = f"https://alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NVDA&apikey={MY_KEY}"

def fetch_data():
    print(f"Attempting Alpha Vantage for {SYMBOL}...")
    response = requests.get(URL)
    data = response.json()

    if "Time Series (Daily)" in data:
        df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient='index')
        df.to_csv("NVDA_test_automation.csv")
        print("Success via Alpha Vantage!")
    else:
        print("Alpha Vantage limit reached. Falling back to Yahoo Finance...")
        # Imperial Stats tip: yfinance is great for quick historical pulls
        ticker = yf.Ticker(SYMBOL)
        df = ticker.history(period="1mo")
        df.to_csv("NVDA_test_automation.csv")
        print("Success via Yahoo Finance!")

if __name__ == "__main__":
    fetch_data()
