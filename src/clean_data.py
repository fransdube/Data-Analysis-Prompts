import pandas as pd
import os

DATA_URL = "https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"
OUTPUT_PATH = "data/cleaned_us_data.csv"

def clean_data():
    print(f"Loading data from {DATA_URL}...")
    # Load directly from URL
    try:
        df = pd.read_csv(DATA_URL)
    except Exception as e:
        print(f"Error downloading data: {e}")
        return

    print("Columns:", df.columns.tolist())

    # Standardize column names if needed
    if 'country' in df.columns and 'location' not in df.columns:
        df.rename(columns={'country': 'location'}, inplace=True)

    print("Filtering for United States...")
    if 'location' not in df.columns:
        print("Error: 'location' column not found.")
        return

    us_data = df[df['location'] == 'United States'].copy()

    if us_data.empty:
        print("Warning: No data found for 'United States'. Checking unique locations...")
        print(df['location'].unique()[:10])
        return

    print("Converting dates...")
    us_data['date'] = pd.to_datetime(us_data['date'])

    print("Handling missing values...")
    # Fill NaNs in cases/deaths with 0
    cols_to_fill = ['new_cases', 'new_deaths', 'total_cases', 'total_deaths']
    for col in cols_to_fill:
        if col in us_data.columns:
            us_data[col] = us_data[col].fillna(0)

    # Select relevant columns
    relevant_cols = ['date', 'location', 'new_cases', 'new_deaths',
                     'total_cases', 'total_deaths', 'hosp_patients',
                     'weekly_hosp_admissions', 'icu_patients', 'population', 'new_cases_smoothed', 'new_deaths_smoothed']

    # Keep only columns that exist
    existing_cols = [c for c in relevant_cols if c in us_data.columns]
    us_data = us_data[existing_cols]

    print(f"Saving cleaned data to {OUTPUT_PATH}...")
    us_data.to_csv(OUTPUT_PATH, index=False)
    print("Done.")

if __name__ == "__main__":
    clean_data()
