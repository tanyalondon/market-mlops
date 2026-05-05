import pandas as pd
import matplotlib.pyplot as plt

def create_chart():
    try:
        df = pd.read_csv("NVDA_test_automation.csv", index_col=0, parse_dates=True)
        df = df.sort_index()

        # THE FIX: Automatically find the column that represents "Close"
        # Most APIs use some variation of 'close'
        close_col = [col for col in df.columns if 'close' in col.lower()][0]
        print(f"Using column: {close_col}")

        # 2. Statistical Calculation: 7-Day Moving Average
        df['7-Day MA'] = df[close_col].rolling(window=7).mean()

        # 3. Plotting
        plt.figure(figsize=(12, 6))
        plt.plot(df.index, df[close_col], label='Daily Price', alpha=0.5)
        plt.plot(df.index, df['7-Day MA'], label='7-Day Moving Average', color='orange')
        
        plt.title('NVIDIA (NVDA) Trend Analysis')
        plt.legend()
        plt.savefig("nvda_trend_chart.png")
        print("Success! Created 'nvda_trend_chart.png'")

    except Exception as e:
        print(f"Error creating chart: {e}")



if __name__ == "__main__":
    create_chart()

