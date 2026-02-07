import pandas as pd
from .config import SELECTED_COUNTRIES

class Preprocessor:
    def filter_countries(self, df):
        if SELECTED_COUNTRIES:
            return df[df['Country'].isin(SELECTED_COUNTRIES)]
        return df
        
    def create_pivot_table(self, df):
        pivot_df = df.pivot(index='Year', columns='Country', values='Population')
        return pivot_df
