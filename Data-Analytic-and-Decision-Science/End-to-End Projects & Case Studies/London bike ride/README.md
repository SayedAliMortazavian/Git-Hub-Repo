# London Bike-Sharing Demand Forecasting & System Dynamics Analysis

## Overview
This repository contains a professional portfolio analysis of the London bike-sharing system, demonstrating an end-to-end workflow from data acquisition and cleaning to advanced forecasting and system dynamics modeling. The project leverages:

- **Python (Pandas, Kaggle API)** for automated data extraction, transformation, and feature engineering.
- **Tableau** (scripts not included) for interactive dashboard development, enabling dynamic exploration of ridership trends, weather impacts, and demand patterns.
- **Statistical Forecasting** (seasonal decomposition, SARIMA) to predict daily ridership volumes with high accuracy.
- **System Dynamics** simulation to evaluate operational policies such as fleet expansion and docking infrastructure investments, identifying feedback delays and capacity saturation points.

All code and supporting artifacts are organized for easy navigation and reproduction of results. This case study is designed to inform data-driven decision-making for operations planning and strategic investment in urban bike-sharing programs.

---

## Scripts
Below is a description of each primary Python script in this repository. All scripts assume you have the necessary Python dependencies installed (see **Getting Started**).

1. **`data_pipeline.py`**
   - **Purpose:** Automates the end-to-end data pipeline:
     1. Downloads the raw London bike-sharing dataset via the Kaggle API.
     2. Extracts and reads the CSV into a Pandas DataFrame.
     3. Renames columns for clarity and performs feature engineering (e.g., converting timestamps, mapping categorical codes, computing humidity fractions).
     4. Exports the cleaned dataset to `London_bikes_final.xlsx` for downstream use (Tableau and forecasting).
   - **Key Outputs:**
     - `London_bikes_final.xlsx` (cleaned dataset)

2. **`forecast_analysis.py`**
   - **Purpose:** Conducts time-series analysis and forecasting:
     1. Loads `London_bikes_final.xlsx` and aggregates hourly ridership into daily totals.
     2. Performs seasonal-trend decomposition (weekly seasonal cycle) to isolate trend and residual components.
     3. Uses `pmdarima.auto_arima` to identify optimal SARIMA parameters for forecasting daily ridership.
     4. Fits a SARIMA model on historical data (excluding the last 30 days), then forecasts the final 30 days.
     5. Evaluates forecast accuracy using MAPE (Mean Absolute Percentage Error) and RMSE (Root Mean Squared Error).
     6. Generates and saves two plots: `seasonal_decomposition.png` and `forecast_vs_actual.png`.
     7. Serializes the fitted SARIMA model to `sarima_model.pkl` for future reuse.
   - **Key Outputs:**
     - `seasonal_decomposition.png` (decomposition plot)
     - `forecast_vs_actual.png` (actual vs. forecast comparison)
     - `sarima_model.pkl` (serialized SARIMA model file)

3. **`sd_model.py`**
   - **Purpose:** Implements a System Dynamics simulation of the bike-sharing ecosystem:
     1. Defines stocks: Available Bikes (AB), In-Use Bikes (UB), and Bikes Under Maintenance (BM).
     2. Defines flows: Rent_Rate, Return_Rate, Maintenance_Rate, Repair_Rate, and Rebalance_Rate.
     3. Simulates hourly dynamics over a 30-day period under two policy scenarios:
        - **Fleet Expansion:** 20% increase in total bike count.
        - **Infrastructure Investment:** 50 additional docking stations (capacity does not directly increase redistribution capacity but affects station saturation).  
     4. Computes the evolution of stock variables each hour, ensuring non-negative values.
     5. Saves simulation outputs to `sd_simulation_results.csv` and a plot of stock trajectories to `sd_simulation_stocks.png`.
   - **Key Outputs:**
     - `sd_simulation_results.csv` (hourly stock values)  
     - `sd_simulation_stocks.png` (plot of stock levels over time)  

---


## Usage: Running the Scripts
### 1. Data Pipeline
```bash
python data_pipeline.py
```
- **Result:** Downloads the London bike-sharing dataset, cleans and transforms it, then writes `London_bikes_final.xlsx` in the current directory.

### 2. Forecast Analysis
```bash
python forecast_analysis.py
```
- **Result:** Reads `London_bikes_final.xlsx`, performs seasonal decomposition and SARIMA forecasting, and saves:
  - `seasonal_decomposition.png`
  - `forecast_vs_actual.png`
  - `sarima_model.pkl` (serialized model)

### 3. System Dynamics Simulation
```bash
python sd_model.py
```
- **Result:** Simulates a 30-day System Dynamics model under fleet-expansion and infrastructure scenarios. Outputs:
  - `sd_simulation_results.csv` (hourly stock levels)  
  - `sd_simulation_stocks.png` (plot of Available Bikes, In-Use Bikes, Under Maintenance over 720 hours)

---



