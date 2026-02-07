from src.data_loader import DataLoader
from src.preprocessing import Preprocessor
from src.feature_engineering import FeatureEngineer
from src.visualization import Visualizer
from src.models import Forecaster
from src.train import Trainer
from src.config import SELECTED_COUNTRIES, FORECAST_YEARS
import pandas as pd
import numpy as np

def main():
    print("=== Global Population Growth Analytics ===")
    
    loader = DataLoader()
    original_df = loader.load_data()
    original_df = loader.clean_data(original_df)
    
    preprocessor = Preprocessor()
    df_filtered = preprocessor.filter_countries(original_df)
    pivot_df = preprocessor.create_pivot_table(df_filtered)
    print(f"Time Series Shape: {pivot_df.shape}")
    
    viz = Visualizer()
    viz.plot_time_series(pivot_df, "Historical Population Trend")
    
    fe = FeatureEngineer()
    growth_df = fe.calculate_growth_rate(pivot_df)
    viz.plot_time_series(growth_df, "Population Growth Rate")
    
    forecaster = Forecaster()
    trainer = Trainer()
    
    print("\n--- Forecasting Future Population ---")
    for country in pivot_df.columns:
        series = pivot_df[country].dropna()
        if len(series) < 10:
            continue
            
        train_size = int(len(series) * 0.8)
        train, test = series.iloc[:train_size], series.iloc[train_size:]
        
        model = forecaster.train_linear_model(train)
        pred = forecaster.predict_linear(model, test.index)
        
        mae, rmse = trainer.evaluate_forecast(test.values, pred)
        print(f"{country} - MAE: {mae:.2f}, RMSE: {rmse:.2f}")
        
        viz.plot_forecast(train, test, pred, country)
        
        if country == 'United States':
            trainer.save_model(model, 'us_linear_model.pkl')

    print("\n=== Analysis Completed ===")

if __name__ == "__main__":
    main()
