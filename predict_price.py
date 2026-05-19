import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import datetime

def train_and_predict():
    try:
        # 1. Load your automated data
        df = pd.read_csv("NVDA_test_automation.csv", index_col=0, parse_dates=True)
        df = df.sort_index()

        # 2. Feature Engineering: Convert dates to a numerical 'Day' count
        # This is a simple but effective way to model time-series trends
        df['Day_Count'] = np.arange(len(df))
        
        # Automatically find the column that represents "Close"
        # Most APIs use some variation of 'close'
        close_col = [col for col in df.columns if 'close' in col.lower()][0]
        print(f"Using column: {close_col}")

        X = df[['Day_Count']].values
        y = df[close_col].values # Or your detected close column

        # 3. Train the Model (The "Imperial" Brain)
        model = LinearRegression()
        model.fit(X, y)

        # 4. Predict Tomorrow
        next_day_index = np.array([[len(df)]])
        prediction = model.predict(next_day_index)[0]

        # 5. Evaluate: How well did the line fit?
        # Recruiter tip: R2 and MAE prove you care about performance, not just theory
        r2 = r2_score(y, model.predict(X))
        print(f"Prediction for Tomorrow: ${prediction:.2f}")
        print(f"Model Confidence (R2): {r2:.4f}")

        # Save prediction to a file for the bot to read
        with open("prediction_results.txt", "w") as f:
            f.write(f"Tomorrow's Predicted Price: ${prediction:.2f}\n")
            f.write(f"Model R2 Score: {r2:.4f}")

    except Exception as e:
        print(f"ML Error: {e}")

if __name__ == "__main__":
    train_and_predict()
