### data_pipeline.py
```python
import os
import zipfile
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# 1. Authenticate and download dataset
api = KaggleApi()
api.authenticate()

# Specify dataset identifier
DATASET_IDENTIFIER = 'hcbecker/london-bike-sharing-dataset'
DOWNLOAD_PATH = './'
ZIP_FILENAME = 'london-bike-sharing-dataset.zip'

# Download without extracting
api.dataset_download_files(DATASET_IDENTIFIER, path=DOWNLOAD_PATH, unzip=False)

# 2. Unzip the downloaded file
with zipfile.ZipFile(os.path.join(DOWNLOAD_PATH, ZIP_FILENAME), 'r') as zf:
    zf.extractall(path=DOWNLOAD_PATH)

# 3. Load CSV into DataFrame
CSV_FILENAME = 'london_merged.csv'
raw_path = os.path.join(DOWNLOAD_PATH, CSV_FILENAME)
bikes = pd.read_csv(raw_path)

# 4. Data Cleaning & Feature Engineering
# Rename columns for clarity
bikes = bikes.rename(columns={
    'cnt': 'total_rides',
    't1': 'temp_actual_c',
    't2': 'temp_feelslike_c',
    'hum': 'humidity_pct',
    'wind_speed': 'wind_kph',
    'is_holiday': 'holiday_flag',
    'is_weekend': 'weekend_flag',
    'season': 'season_code',
    'weather_code': 'weather_code'
})

# Convert humidity percentage to fraction
bikes['humidity_pct'] = bikes['humidity_pct'] / 100.0

# Map season_code and weather_code to descriptive labels
season_map = {0: 'Winter', 1: 'Spring', 2: 'Summer', 3: 'Autumn'}
bikes['season'] = bikes['season_code'].map(season_map)

weather_map = {
    1: 'Clear', 2: 'Partly Cloudy', 3: 'Cloudy', 4: 'Rain',
    7: 'Snow', 10: 'Fog', 26: 'Thunderstorm'
}
bikes['weather'] = bikes['weather_code'].map(weather_map)

# Convert timestamp to datetime and extract features
bikes['timestamp'] = pd.to_datetime(bikes['timestamp'])
bikes['date'] = bikes['timestamp'].dt.date
bikes['hour'] = bikes['timestamp'].dt.hour
bikes['year'] = bikes['timestamp'].dt.year
bikes['month'] = bikes['timestamp'].dt.month
bikes['day_of_week'] = bikes['timestamp'].dt.day_name()

# 5. Write cleaned data to Excel for Tableau
OUTPUT_EXCEL = 'London_bikes_final.xlsx'
bikes.to_excel(OUTPUT_EXCEL, sheet_name='Data', index=False)
print(f"Data pipeline complete. Cleaned data written to {OUTPUT_EXCEL}.")
```

