import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np


actual_df = pd.read_csv("../data/forecast_results.csv")

y_true = actual_df['yhat'][:-12]
y_pred = actual_df['yhat'][-12:]

mae = mean_absolute_error(y_true[-12:], y_pred)
rmse = np.sqrt(mean_squared_error(y_true[-12:], y_pred))
mape = np.mean(np.abs((y_true[-12:] - y_pred) / y_true[-12:])) * 100

print(f"MAE: {mae}")
print(f"RMSE: {rmse}")
print(f"MAPE: {mape}")