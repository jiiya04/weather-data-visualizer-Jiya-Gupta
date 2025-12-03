# weather-data-visualizer-Jiya-Gupta
## Overview
This project performs basic weather data analysis using Python.  
It includes data cleaning, statistical analysis, visualizations, grouping, and exporting results.

The dataset used is **weather.csv**, containing daily weather information:

- Date  
- Temperature (°C)  
- Humidity (%)  
- Wind Speed (km/h)  
- Precipitation (mm)

---

## Features

### 1. Data Loading
- Reads `weather.csv`
- Displays head, data types, missing values, shape

### 2. Data Cleaning
- Converts Date column to datetime format
- Sets Date as index
- Produces a clean DataFrame for analysis

### 3. Statistical Analysis
- Computes daily mean, min, max, standard deviation using NumPy
- Generates weekly, monthly, and yearly aggregates using `resample()` and `groupby()`

### 4. Visualizations
The script generates and saves the following:
- `temperature.png` – Temperature trend  
- `humidity.png` – Humidity trend  
- `temp_vs_humidity.png` – Temperature vs Humidity scatter plot  
- `correlation_heatmap.png` – Correlation matrix heatmap  

---

## 5. Exporting Results
- Cleaned dataset saved as **weather_cleaned.csv**
- A short markdown analysis report saved as **report.md**

---

## How to Run
1. Ensure `weather.csv` is in the same folder as the script.  
2. Run:

3. All output files will appear in the same folder.

---

## Output Files
- weather_cleaned.csv  
- temperature.png  
- humidity.png  
- temp_vs_humidity.png  
- correlation_heatmap.png  
- report.md  

---

## Notes
- Dataset contains only 7 days, so monthly and yearly results reflect the available data only.

