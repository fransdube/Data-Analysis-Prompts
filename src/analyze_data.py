import pandas as pd
import numpy as np
from scipy import stats

INPUT_FILE = 'data/cleaned_us_data.csv'

def analyze_data():
    print("Loading cleaned data...")
    df = pd.read_csv(INPUT_FILE)
    df['date'] = pd.to_datetime(df['date'])

    # 2. Calculate monthly new cases for US in 2023
    print("\n--- Question 1: Peak Infection Month in 2023 ---")
    df_2023 = df[df['date'].dt.year == 2023].copy()

    if df_2023.empty:
        print("No data available for 2023.")
    else:
        # Group by month
        monthly_cases = df_2023.groupby(df_2023['date'].dt.to_period('M'))['new_cases'].sum()

        print("\nMonthly New Cases (2023):")
        print(monthly_cases)

        # 3. Find peak month and value
        peak_month = monthly_cases.idxmax()
        peak_value = monthly_cases.max()

        print(f"\nPeak Month: {peak_month}")
        print(f"Peak Cases: {peak_value:,.0f}")

    # 4. Hospitalization Analysis
    # Note: The dataset might not have age-specific hospitalization data (hosp_patients is usually total).
    # The prompt asks for "hospitalization rates by age group".
    # Since the OWID compact dataset usually lacks age-stratified hospitalization data,
    # I will check if I can infer something or state the limitation.
    # However, to satisfy the prompt's request for "code to answer", I will implement a placeholder
    # analysis or use the 'hosp_patients' (total) if age data is missing, and explain.

    print("\n--- Question 2: Hospitalization Analysis ---")
    if 'age_group' in df.columns:
        # If we had age groups (we don't in the compact set usually)
        pass
    else:
        print("Note: Dataset does not contain age-stratified hospitalization data.")
        print("Analyzing total hospitalization trends instead.")

        # Calculate hospitalization rate (patients / population * 100k)
        # using 'hosp_patients' (daily count) or 'weekly_hosp_admissions'

        if 'weekly_hosp_admissions' in df.columns and df['weekly_hosp_admissions'].notna().sum() > 0:
            avg_weekly_hosp = df['weekly_hosp_admissions'].mean()
            print(f"Average Weekly Hospital Admissions: {avg_weekly_hosp:,.0f}")

            # Find peak hospitalization period
            peak_hosp_date = df.loc[df['weekly_hosp_admissions'].idxmax(), 'date']
            peak_hosp_val = df['weekly_hosp_admissions'].max()
            print(f"Peak Weekly Admissions: {peak_hosp_val:,.0f} on {peak_hosp_date.date()}")

    # 6. Statistical Analysis Enhancement
    print("\n--- Statistical Enhancements ---")

    # 1. Moving Averages
    df['cases_7day_ma'] = df['new_cases'].rolling(window=7).mean()
    df['deaths_7day_ma'] = df['new_deaths'].rolling(window=7).mean()

    print("Calculated 7-day moving averages for cases and deaths.")

    # 2. Correlation between cases and deaths
    # We use smoothed data or moving averages to reduce noise
    corr, p_val = stats.pearsonr(df['new_cases_smoothed'].fillna(0), df['new_deaths_smoothed'].fillna(0))
    print(f"\nCorrelation between Smoothed Cases and Deaths: {corr:.4f} (p-value: {p_val:.4e})")

    if p_val < 0.05:
        print("The correlation is statistically significant.")
    else:
        print("The correlation is not statistically significant.")

    # 4. Mortality Rate (Case Fatality Rate - CFR)
    # CFR = Total Deaths / Total Cases (Naive) or sum of deaths / sum of cases in a period
    total_cases = df['new_cases'].sum()
    total_deaths = df['new_deaths'].sum()
    if total_cases > 0:
        cfr = (total_deaths / total_cases) * 100
        print(f"\nOverall Case Fatality Rate (CFR): {cfr:.2f}%")

    # Trend Analysis (Simple Linear Regression on 2023 cases)
    if not df_2023.empty:
        # Create a numerical time index
        df_2023['time_idx'] = np.arange(len(df_2023))
        slope, intercept, r_value, p_value, std_err = stats.linregress(df_2023['time_idx'], df_2023['new_cases'])

        print(f"\n2023 Cases Trend Slope: {slope:.2f} cases/day")
        if slope > 0:
            print("Trend: Increasing")
        else:
            print("Trend: Decreasing")
        print(f"R-squared: {r_value**2:.4f}")

if __name__ == "__main__":
    analyze_data()
