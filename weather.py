# weather_analysis_

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# === User setting: show plots on screen(True = show, False = only save files) ===
SHOW_PLOTS = False

# ---------------------------
# TASK 1: Load CSV and inspect
# ---------------------------
df = pd.read_csv("weather.csv")

print("=== HEAD (first 10 rows) ===")
print(df.head(10).to_string(index=False))

print("\n=== COLUMNS & DTYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES (per column) ===")
print(df.isnull().sum())

print("\n=== SHAPE ===")
print(df.shape)

# ---------------------------
# TASK 2: Cleaning & preprocessing
# ---------------------------
# Convert Date to datetime, set as index
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

print("\nConverted Date to datetime and set as index.")
print(df.dtypes)

# ---------------------------
# TASK 3: EDA & Statistics
# ---------------------------
print("\n=== SUMMARY STATISTICS (describe) ===")
print(df.describe().to_string())

print("\n=== MEDIANS ===")
print(df.median().to_string())

# Simple daily statistics using NumPy (per-column)
print("\n=== DAILY STATS (mean, min, max, std) using NumPy ===")
print("Mean:\n", np.round(df.mean(), 3).to_string())
print("Min:\n", df.min().to_string())
print("Max:\n", df.max().to_string())
print("Std:\n", np.round(df.std(), 3).to_string())

# Monthly and yearly: use resample (works even for small data)
monthly = df.resample('M').agg(['mean','min','max','std'])
weekly = df.resample('W').agg(['mean','min','max','std'])
yearly = df.resample('Y').agg(['mean','min','max','std'])  # will be same as monthly for small dataset

print("\n=== MONTHLY AGGREGATES (mean,min,max,std) ===")
print(monthly.to_string())

print("\n=== WEEKLY AGGREGATES (mean,min,max,std) ===")
print(weekly.to_string())

print("\n=== YEARLY AGGREGATES (mean,min,max,std) ===")
print(yearly.to_string())

# Also demonstrate groupby month (useful if dataset spans months)
df['Month'] = df.index.month
group_by_month = df.groupby('Month').agg(['mean','min','max','std'])
print("\n=== GROUP BY MONTH ===")
print(group_by_month.to_string())

# Remove the temporary Month column from df for later steps
df = df.drop(columns=['Month'])

# ---------------------------
# TASK 4: Visualizations 
# ---------------------------
def save_plot(fig_name, show=SHOW_PLOTS):
    plt.tight_layout()
    plt.savefig(fig_name)
    print(f"Saved: {fig_name}")
    if show:
        plt.show()
    plt.close()

# Temperature plot
plt.figure(figsize=(8,4))
plt.plot(df.index, df['Temperature'], marker='o')
plt.title("Temperature Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
save_plot("temperature.png")

# Humidity plot
plt.figure(figsize=(8,4))
plt.plot(df.index, df['Humidity'], marker='o')
plt.title("Humidity Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.grid(True)
save_plot("humidity.png")

# Scatter plot Temperature vs Humidity
plt.figure(figsize=(6,4))
plt.scatter(df['Temperature'], df['Humidity'])
plt.title("Temperature vs Humidity")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.grid(True)
save_plot("temp_vs_humidity.png")

# Correlation heatmap (numeric columns only)
num_cols = df.select_dtypes(include=[np.number])
corr = num_cols.corr()

plt.figure(figsize=(6,5))
plt.imshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar(label='Correlation (−1 to 1)')
cols = corr.columns.tolist()
plt.xticks(range(len(cols)), cols, rotation=45)
plt.yticks(range(len(cols)), cols)
# annotate numbers
for i in range(len(cols)):
    for j in range(len(cols)):
        plt.text(j, i, f"{corr.iloc[i, j]:.2f}", ha='center', va='center', fontsize=9)
plt.title("Correlation Heatmap")
save_plot("correlation_heatmap.png")

print("\nPlots saved: temperature.png, humidity.png, temp_vs_humidity.png, correlation_heatmap.png")


# ---------------------------
# TASK 6: Export and Storytelling
# ---------------------------
# Export cleaned data
df.to_csv("weather_cleaned.csv", index=True)
print("Saved: weather_cleaned.csv")

# Create a short markdown report
report_text = f"""# Weather Data Analysis - Short Report

**Dataset:** weather_cleaned.csv (rows: {df.shape[0]}, cols: {df.shape[1]})

## Key summary
- Avg Temperature: {df['Temperature'].mean():.2f} °C
- Min Temperature: {df['Temperature'].min():.2f} °C
- Max Temperature: {df['Temperature'].max():.2f} °C
- Avg Humidity: {df['Humidity'].mean():.1f} %
- Avg WindSpeed: {df['WindSpeed'].mean():.1f} km/h

## Correlations (numeric columns)
{corr.to_string()}

## Files saved:
- temperature.png
- humidity.png
- temp_vs_humidity.png
- correlation_heatmap.png
- weather_cleaned.csv

*Note:* Dataset contains a short period (7 days), so monthly/yearly aggregates are based on available data.
"""

with open("report.md", "w", encoding="utf-8") as f:
    f.write(report_text)
print("Saved: report.md")

print("\nALL TASKS COMPLETE. Check the folder for output files.")
