from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
import pandas as pd

class Forecaster:
    def train_linear_model(self, series):
        X = np.array(series.index).reshape(-1, 1)
        y = series.values
        model = LinearRegression()
        model.fit(X, y)
        return model

    def train_arima(self, series, order=(5,1,0)):
        try:
            model = ARIMA(series, order=order)
            model_fit = model.fit()
            return model_fit
        except:
             return None

    def predict_linear(self, model, years):
        X_future = np.array(years).reshape(-1, 1)
        return model.predict(X_future)
