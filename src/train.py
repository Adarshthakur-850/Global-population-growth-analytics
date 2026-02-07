from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import pickle
import os
from .config import MODELS_DIR

class Trainer:
    def evaluate_forecast(self, y_true, y_pred):
        mae = mean_absolute_error(y_true, y_pred)
        rmse = np.sqrt(mean_squared_error(y_true, y_pred))
        return mae, rmse

    def save_model(self, model, filename):
        path = os.path.join(MODELS_DIR, filename)
        with open(path, 'wb') as f:
            pickle.dump(model, f)
        print(f"Saved model: {path}")
