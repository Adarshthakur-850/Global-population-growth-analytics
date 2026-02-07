import pandas as pd
from .config import DATA_URL

class DataLoader:
    def load_data(self):
        print("Loading data from URL...")
        df = pd.read_csv(DATA_URL)
        return df

    def clean_data(self, df):
        print("Cleaning data...")
        if 'Country Name' in df.columns:
            df = df.rename(columns={'Country Name': 'Country', 'Value': 'Population'})
            
        df = df.dropna()
        return df
