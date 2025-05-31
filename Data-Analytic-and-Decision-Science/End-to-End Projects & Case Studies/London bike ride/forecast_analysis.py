### forecast_analysis.py
```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
from pmdarima import auto_arima
import matplotlib.pyplot as plt

# 1. Load cleaned data
EXCEL_PATH = 'London_bikes_final.xlsx'
bikes = pd.read_excel(EXCEL_PATH, sheet_name='Data')

# 2. Aggregate hourly rides into daily totals
daily_rides = bikes.groupby('date')['total_rides'].sum()

# 3. Seasonal decomposition
decomposition = sm.tsa.seasonal_decompose(daily_rides, model='additive', period=7)
fig = decomposition.plot()
fig.set_size_inches(10, 8)
plt.tight_layout()
plt.savefig('seasonal_decomposition.png')
plt.close()

# 4. SARIMA (Seasonal ARIMA) Model
# Split into train and test (last 30 days for testing)
train = daily_rides.iloc[:-30]
test = daily_rides.iloc[-30:]

# Auto ARIMA for best parameters
auto_model = auto_arima(
    train,
    seasonal=True,
    m=7,  # weekly seasonality
    trace=True,
    error_action='ignore',
    suppress_warnings=True
)
print(auto_model.summary())

# Fit final model
dates = train.index
arima_model = sm.tsa.statespace.SARIMAX(
    train,
    order=auto_model.order,
    seasonal_order=auto_model.seasonal_order,
    enforce_stationarity=False,
    enforce_invertibility=False
).fit(disp=False)

# Forecast next 30 days
forecast = arima_model.get_forecast(steps=30)
forecast_ci = forecast.conf_int()

# 5. Evaluation Metrics (MAPE, RMSE)
pred = forecast.predicted_mean
actual = test.values
mape = np.mean(np.abs((actual - pred) / actual)) * 100
mse = np.sqrt(np.mean((actual - pred)**2))
print(f'MAPE: {mape:.2f}%, RMSE: {rmse:.2f}')

# 6. Plot actual vs. forecast
plt.figure(figsize=(10, 5))
plt.plot(train.index, train, label='Train')
plt.plot(test.index, test, label='Actual')
plt.plot(test.index, pred, label='Forecast', linestyle='--')
plt.fill_between(
    test.index,
    forecast_ci.iloc[:, 0],
    forecast_ci.iloc[:, 1],
    color='lightgrey', alpha=0.3
)
plt.xlabel('Date')
plt.ylabel('Daily Rides')
plt.title('SARIMA Forecast vs. Actual (Last 30 days)')
plt.legend()
plt.tight_layout()
plt.savefig('forecast_vs_actual.png')
plt.close()

# 7. Save model for future use
arima_model.save('sarima_model.pkl')
print('Forecasting analysis complete. Model and figures saved.')
```
