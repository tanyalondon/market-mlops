import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression



def create_chart():
    try:
        df = pd.read_csv("NVDA_test_automation.csv", index_col=0, parse_dates=True)
        df = df.sort_index()
        close_col = [col for col in df.columns if 'close' in col.lower()][0]

        # 1. Prepare Data for Regression Line
        # We need numerical X values to calculate the line of best fit
        X = np.arange(len(df)).reshape(-1, 1)
        y = df[close_col].values
        model = LinearRegression().fit(X, y)
        trend_line = model.predict(X)

        # 2. Plotting
        plt.figure(figsize=(12, 6))
        plt.plot(df.index, y, label='Actual Price', alpha=0.5, color='blue')
        plt.plot(df.index, trend_line, label='Statistical Trend (Regression)', color='red', linestyle='--')
        
        plt.title('NVIDIA (NVDA) Market Trend Analysis')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid(True, alpha=0.3)

        plt.savefig("nvda_trend_chart.png")
        print("Success! Updated chart with Regression Trend.")

    except Exception as e:
        print(f"Error: {e}")
