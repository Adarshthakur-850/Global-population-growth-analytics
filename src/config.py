import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLOTS_DIR = os.path.join(BASE_DIR, 'plots')
MODELS_DIR = os.path.join(BASE_DIR, 'models')

os.makedirs(PLOTS_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)

DATA_URL = "https://raw.githubusercontent.com/datasets/population/main/data/population.csv"

SELECTED_COUNTRIES = ['United States', 'China', 'India', 'Japan', 'Germany', 'Brazil', 'Nigeria']
FORECAST_YEARS = 20
