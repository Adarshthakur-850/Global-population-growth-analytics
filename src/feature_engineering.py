import pandas as pd

class FeatureEngineer:
    def calculate_growth_rate(self, df):
        print("Calculating growth rates...")
        growth_rate = df.pct_change() * 100
        return growth_rate
    
    def calculate_rolling_average(self, df, window=5):
        print(f"Calculating {window}-year rolling average...")
        return df.rolling(window=window).mean()
