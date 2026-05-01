import requests
import pandas as pd

# 1. Paste your key inside these quotes
MY_KEY = '0P5RS30RBWGCEWFI'
 

# This is a solid, pre-built link. Do not change anything but the API key at the end.
URL = f"https://alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NVDA&apikey={MY_KEY}"

def fetch_data():
    print("Connecting to Alpha Vantage...")
    try:
        response = requests.get(URL)
        data = response.json()
        
        # Check if the API returned a valid time series
        if "Time Series (Daily)" in data:
            df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient='index')
            df.to_csv("NVDA_data.csv")
            print("Success! 'NVDA_data.csv' has been created on your Desktop.")
        else:
            print("The API connected, but didn't return data. Message from Alpha Vantage:")
            print(data)
            
    except Exception as e:
        print(f"Connection Error: {e}")
        print("Tip: Check if your Mac is connected to the internet and the URL is correct.")

if __name__ == "__main__":
    fetch_data()
