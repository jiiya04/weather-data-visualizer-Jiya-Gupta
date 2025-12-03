# Weather Data Analysis - Short Report

**Dataset:** weather_cleaned.csv (rows: 7, cols: 4)

## Key summary
- Avg Temperature: 24.90 °C
- Min Temperature: 22.90 °C
- Max Temperature: 27.30 °C
- Avg Humidity: 58.9 %
- Avg WindSpeed: 12.0 km/h

## Correlations (numeric columns)
               Temperature  Humidity  WindSpeed  Precipitation
Temperature       1.000000 -0.990910  -0.718166      -0.548595
Humidity         -0.990910  1.000000   0.779293       0.637272
WindSpeed        -0.718166  0.779293   1.000000       0.762001
Precipitation    -0.548595  0.637272   0.762001       1.000000

## Files saved:
- temperature.png
- humidity.png
- temp_vs_humidity.png
- correlation_heatmap.png
- weather_cleaned.csv

*Note:* Dataset contains a short period (7 days), so monthly/yearly aggregates are based on available data.
