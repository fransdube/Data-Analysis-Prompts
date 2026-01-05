import pandas as pd
import matplotlib.pyplot as plt
import os
from statsmodels.tsa.arima.model import ARIMA
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

INPUT_FILE = 'data/cleaned_us_data.csv'
OUTPUT_DIR = 'output'

def advanced_analysis():
    print("Loading data for forecasting...")
    df = pd.read_csv(INPUT_FILE)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    # We will forecast 'new_cases_smoothed' to avoid weekly seasonality noise
    # Filter for the last valid period of data before it drops to zero (if applicable)
    # The user analysis showed 2023 data dropping to zero. Let's forecast based on 2022 data or early 2023.
    # Actually, let's just take the non-zero tail.

    data = df['new_cases_smoothed'].dropna()
    # Filter out the trailing zeros if they exist (reporting stopped)
    data = data[data > 0]

    if data.empty:
        print("No valid data for forecasting.")
        return

    # Use a subset to make it faster/cleaner, e.g., last 365 days of valid data
    train_data = data.tail(365)

    print("Training ARIMA model on last 365 days of reported data...")
    # Simple ARIMA (5,1,0) - Auto-regressive
    model = ARIMA(train_data, order=(5,1,0))
    model_fit = model.fit()

    print(model_fit.summary())

    # Forecast next 30 days
    steps = 30
    forecast = model_fit.forecast(steps=steps)

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(train_data.index, train_data, label='Historical Data (Last 365 Days)')

    # Create forecast index
    forecast_index = pd.date_range(start=train_data.index[-1] + pd.Timedelta(days=1), periods=steps)
    plt.plot(forecast_index, forecast, label='30-Day Forecast', color='red', linestyle='--')

    plt.title('COVID-19 Cases Forecast (ARIMA Model)', fontsize=16)
    plt.xlabel('Date')
    plt.ylabel('New Cases (Smoothed)')
    plt.legend()
    plt.grid(True)

    output_path = os.path.join(OUTPUT_DIR, 'forecast_arima.png')
    plt.savefig(output_path, dpi=300)
    print(f"Forecast plot saved to {output_path}")

if __name__ == "__main__":
    advanced_analysis()
