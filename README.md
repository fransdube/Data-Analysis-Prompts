# COVID-19 Data Analysis Project

## Overview
This project analyzes COVID-19 trends in the United States using data from [Our World in Data (OWID)](https://ourworldindata.org/coronavirus). The analysis focuses on the year 2023, identifying peak infection months, hospitalization trends, and statistical correlations between cases and deaths.

## Dataset
- **Source:** Our World in Data (OWID) COVID-19 Dataset
- **Format:** CSV
- **Content:** Daily records of cases, deaths, hospitalizations, testing, and vaccinations by country.
- **Preprocessing:** The dataset is filtered for the "United States" and cleaned to handle missing values and date formats.

## Research Questions
1. **What was the peak infection month for the United States in 2023?**
   - *Methodology:* Aggregated daily new cases by month.
2. **What are the hospitalization trends?**
   - *Methodology:* Analyzed weekly hospital admission rates over time.
3. **Is there a correlation between cases and deaths?**
   - *Methodology:* Calculated Pearson correlation coefficient on 7-day smoothed data.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repo_url>
   cd <repo_name>
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas matplotlib scipy
   ```

3. **Run the analysis:**
   ```bash
   # Clean the data (downloads from OWID)
   python src/clean_data.py

   # Run statistical analysis
   python src/analyze_data.py

   # Generate visualizations
   python src/visualize_data.py

   # Run advanced analysis (Forecasting)
   python src/advanced_analysis.py
   ```

## Results Summary

- **Peak Infection Month (2023):** January 2023 saw the highest number of new cases.
- **Hospitalizations:** Significant peaks observed in early 2022, with a general downward trend in 2023.
- **Correlation:** A strong positive correlation exists between new cases and new deaths ($p < 0.05$).

### Visualizations
Charts are saved in the `output/` directory:
- `us_monthly_cases_2023.png`
- `us_hospital_admissions.png`
- `cases_vs_deaths_comparison.png`
- `forecast_arima.png`

## Project Structure
- `data/`: Contains downloaded and cleaned data (ignored in git).
- `src/`: Python scripts for cleaning, analysis, and visualization.
- `notebooks/`: Jupyter notebook for interactive analysis.
- `output/`: Generated charts and figures.

## Future Work
- Enhance forecasting models with Prophet or LSTM.
- Compare US trends with other major nations.
- Incorporate vaccination data into the correlation analysis.
