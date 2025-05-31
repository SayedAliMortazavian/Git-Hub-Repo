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
