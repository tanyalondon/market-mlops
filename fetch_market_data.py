import os
import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

MY_KEY = os.getenv('ALPHAVANTAGE_API_KEY')

# 1. Paste your key inside these quotes
 

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
            df.to_csv("NVDA_test_automation.csv") #("NVDA_data.csv")
            print("Success! 'NVDA_data.csv' has been created on your Desktop.")
        else:
            print("The API connected, but didn't return data. Message from Alpha Vantage:")
            print(data)
            
    except Exception as e:
        print(f"Connection Error: {e}")
        print("Tip: Check if your Mac is connected to the internet and the URL is correct.")

if __name__ == "__main__":
    fetch_data()
