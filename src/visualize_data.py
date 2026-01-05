import pandas as pd
import matplotlib.pyplot as plt
import os

INPUT_FILE = 'data/cleaned_us_data.csv'
OUTPUT_DIR = 'output'

def visualize_data():
    print("Loading data...")
    df = pd.read_csv(INPUT_FILE)
    df['date'] = pd.to_datetime(df['date'])

    # Filter for 2023
    df_2023 = df[df['date'].dt.year == 2023].copy()

    # 1. Line Chart: Monthly COVID-19 Cases in US (2023)
    print("Generating Monthly Cases Chart...")
    monthly_cases = df_2023.groupby(df_2023['date'].dt.to_period('M'))['new_cases'].sum()
    monthly_cases.index = monthly_cases.index.astype(str)

    plt.figure(figsize=(12, 6))
    plt.plot(monthly_cases.index, monthly_cases.values, marker='o', linestyle='-', color='b', linewidth=2, label='New Cases')
    plt.title('Monthly COVID-19 Cases in US (2023)', fontsize=16)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('New Cases', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'us_monthly_cases_2023.png'), dpi=300)
    plt.close()

    # 2. Hospitalization Trends (Since we don't have age groups)
    # We will plot weekly hospital admissions over the full period
    print("Generating Hospitalization Trends Chart...")
    plt.figure(figsize=(12, 6))
    # Filter out NaNs for plotting
    hosp_data = df.dropna(subset=['weekly_hosp_admissions'])
    plt.plot(hosp_data['date'], hosp_data['weekly_hosp_admissions'], color='red', label='Weekly Admissions')

    plt.title('Weekly COVID-19 Hospital Admissions in US', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Admissions', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'us_hospital_admissions.png'), dpi=300)
    plt.close()

    # 3. Subplot: Cases vs Deaths (7-day MA)
    print("Generating Comparative Subplot...")
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

    # Calculate MAs if not present (though clean_data has 'smoothed' columns)
    # The 'new_cases_smoothed' is 7-day MA provided by OWID

    ax1.plot(df['date'], df['new_cases_smoothed'], color='blue', label='7-day Avg Cases')
    ax1.set_title('Daily New Cases (7-day Moving Average)', fontsize=14)
    ax1.set_ylabel('Cases')
    ax1.grid(True, alpha=0.5)
    ax1.legend()

    ax2.plot(df['date'], df['new_deaths_smoothed'], color='black', label='7-day Avg Deaths')
    ax2.set_title('Daily New Deaths (7-day Moving Average)', fontsize=14)
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Deaths')
    ax2.grid(True, alpha=0.5)
    ax2.legend()

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'cases_vs_deaths_comparison.png'), dpi=300)
    plt.close()

    print("Visualizations saved to 'output/' directory.")

if __name__ == "__main__":
    visualize_data()
