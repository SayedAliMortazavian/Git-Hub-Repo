

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


### sd_model.py
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# System Dynamics Simulation for Bike-Sharing
# Stocks: Available_Bikes (AB), In_Use_Bikes (UB), Under_Maintenance (BM)
# Flows: Rent_Rate, Return_Rate, Maint_Rate, Repair_Rate, Rebalance_Rate

# 1. Define Parameters
TOTAL_BIKES_BASE = 1000            # baseline fleet
EXPANSION_FACTOR = 1.20            # 20% expansion
DOCK_STATIONS_BASE = 250           # baseline docking stations
NEW_DOCKS = 50                     # additional docks
AVG_TRIP_DURATION = 0.75           # average trip duration (hours)
MAINTENANCE_RATE = 0.01            # fraction of in-use bikes needing maintenance per hour
AVG_REPAIR_TIME = 10.0             # average repair time (hours)
TRUCK_CAPACITY = 40                # bikes per redistribution truck
NUM_TRUCKS_BASE = 3

# 2. Time settings
time_steps = 24 * 30               # simulate hourly for 30 days
delta_t = 1.0                       # 1 hour time step

# 3. Initialize arrays for stocks
AB = np.zeros(time_steps)   # Available Bikes
UB = np.zeros(time_steps)   # In-Use Bikes
BM = np.zeros(time_steps)   # Bikes Under Maintenance

# Initial conditions
AB[0] = TOTAL_BIKES_BASE
UB[0] = 0
BM[0] = 0

# Weather-based Demand Propensity (simplified constant for simulation)
# In real use, import from actual propensity time-series
DEMAND_PROPENSITY = 0.5      # constant fraction per hour for simulation

# 4. Optional scenario toggles
apply_fleet_expansion = True
apply_infrastructure = True

if apply_fleet_expansion:
    TOTAL_BIKES = TOTAL_BIKES_BASE * EXPANSION_FACTOR
    AB[0] = TOTAL_BIKES
else:
    TOTAL_BIKES = TOTAL_BIKES_BASE

if apply_infrastructure:
    DOCK_STATIONS = DOCK_STATIONS_BASE + NEW_DOCKS
else:
    DOCK_STATIONS = DOCK_STATIONS_BASE

# Adjust redistribution capacity if infrastructure increases
NUM_TRUCKS = NUM_TRUCKS_BASE
# Rebalance capacity unaffected by docks directly

# 5. Simulation loop
time = np.arange(time_steps)
for t in range(1, time_steps):
    # a) Rent_Rate: users who rent bikes this hour
    rent_rate = DEMAND_PROPENSITY * AB[t-1]
    if rent_rate > AB[t-1]:
        rent_rate = AB[t-1]

    # b) Return_Rate: bikes that return
eturn_rate = UB[t-1] / AVG_TRIP_DURATION

    # c) Maintenance: fraction of UB needing service
    maint_rate = MAINTENANCE_RATE * UB[t-1]

    # d) Repair completion: fraction of BM returned
    repair_rate = BM[t-1] / AVG_REPAIR_TIME

    # e) Redistribution: move bikes from surplus to deficit (simplified as constant)
    rebalance_capacity = TRUCK_CAPACITY * NUM_TRUCKS
    rebalance_rate = min(rebalance_capacity, AB[t-1]) if AB[t-1] > rebalance_capacity else 0

    # Update stocks\    AB[t] = AB[t-1] + (return_rate + repair_rate + rebalance_rate) - (rent_rate + maint_rate)
    UB[t] = UB[t-1] + rent_rate - return_rate
    BM[t] = BM[t-1] + maint_rate - repair_rate

    # Ensure non-negative
    AB[t] = max(AB[t], 0)
    UB[t] = max(UB[t], 0)
    BM[t] = max(BM[t], 0)

# 6. Compile results into DataFrame for analysis
results = pd.DataFrame({
    'Hour': time,
    'Available_Bikes': AB,
    'In_Use_Bikes': UB,
    'Under_Maintenance': BM
})

# 7. Plot key stocks over time
plt.figure(figsize=(12, 6))
plt.plot(results['Hour'], results['Available_Bikes'], label='Available Bikes')
plt.plot(results['Hour'], results['In_Use_Bikes'], label='In-Use Bikes')
plt.plot(results['Hour'], results['Under_Maintenance'], label='Under Maintenance')
plt.xlabel('Hour')
plt.ylabel('Number of Bikes')
plt.title('System Dynamics Simulation: Bike-Sharing Stocks')
plt.legend()
plt.tight_layout()
plt.savefig('sd_simulation_stocks.png')
plt.close()

# 8. Save results to CSV
results.to_csv('sd_simulation_results.csv', index=False)
print('System Dynamics simulation complete. Results saved to sd_simulation_results.csv.')
