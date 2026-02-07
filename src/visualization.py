import matplotlib.pyplot as plt
import seaborn as sns
import os
import plotly.express as px
from .config import PLOTS_DIR

class Visualizer:
    def __init__(self):
        sns.set(style="whitegrid")

    def save_plot(self, fig, filename):
        path = os.path.join(PLOTS_DIR, filename)
        fig.savefig(path)
        plt.close(fig)
        print(f"Saved plot: {path}")

    def plot_time_series(self, df, title):
        plt.figure(figsize=(12, 6))
        for col in df.columns:
            plt.plot(df.index, df[col], label=col)
        plt.title(title)
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.legend()
        self.save_plot(plt.gcf(), f'{title.lower().replace(" ", "_")}.png')

    def plot_forecast(self, train, test, forecast, country):
        plt.figure(figsize=(12, 6))
        plt.plot(train.index, train, label='Train')
        plt.plot(test.index, test, label='Test')
        plt.plot(test.index, forecast, label='Forecast', linestyle='--')
        plt.title(f'Population Forecast: {country}')
        plt.legend()
        self.save_plot(plt.gcf(), f'forecast_{country}.png')
