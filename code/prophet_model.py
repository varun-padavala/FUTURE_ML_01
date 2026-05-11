import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
from data_preprocessing import load_and_prepare_data

# load data
df = load_and_prepare_data("../data/Sample - Superstore.csv")

# train model
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
    daily_seasonality=False
)

model.fit(df)

# future prediction (next 12 months)
future = model.make_future_dataframe(periods=12, freq='ME')
forecast = model.predict(future)

# save forecast
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(
    "../data/forecast_results.csv", index=False
)

# plot
plt.figure(figsize=(12,6))
plt.plot(df['ds'], df['y'], label='Actual')
plt.plot(forecast['ds'], forecast['yhat'], label='Forecast', linestyle='--')

plt.fill_between(
    forecast['ds'],
    forecast['yhat_lower'],
    forecast['yhat_upper'],
    alpha=0.2
)

plt.title("Monthly Sales Forecast")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid()

plt.savefig("../visuals/forecast_plot.png")
plt.show()

# components plot
fig2 = model.plot_components(forecast)
fig2.savefig("../visuals/components_plot.png")