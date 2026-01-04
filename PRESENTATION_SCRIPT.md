# Video Presentation Script: COVID-19 Data Analysis

## 1. Introduction (0:00 - 0:30)
**Visual:** Title slide with project name "COVID-19 Data Analysis 2023" and your name.
**Audio:**
"Hello, my name is [Your Name], and this is my presentation on analyzing COVID-19 trends in the United States.
For this project, I selected the comprehensive dataset from Our World in Data, which provides daily updates on cases, deaths, and hospitalizations worldwide.
My goal was to understand the trajectory of the pandemic in 2023, specifically looking at peak infection times and the relationship between cases and severe outcomes like hospitalization and death."

## 2. Methodology (0:30 - 1:30)
**Visual:** Screen recording of `src/clean_data.py` and the `data/` folder structure.
**Audio:**
"To handle the data, I used Python with the Pandas library.
First, I wrote a script to download the latest data directly from OWID's repository.
The raw dataset is quite large, so I immediately filtered it to isolate records for the United States.
I cleaned the data by converting date strings into datetime objects and handling missing values—filling zeros where appropriate for daily counts.
This resulted in a clean, lightweight CSV file ready for analysis."

## 3. Results (1:30 - 3:00)
**Visual:** Show `output/us_monthly_cases_2023.png` then `output/cases_vs_deaths_comparison.png`.
**Audio:**
"Moving on to the results.
My first research question was: 'When was the peak infection month in 2023?'
As you can see in this line chart, January 2023 was the peak, with a sharp decline as we moved into spring. Note that data reporting frequency changed mid-year, leading to apparent zeros in later months.
Next, I analyzed hospitalizations. This red chart shows weekly admissions. We can see the massive spikes in previous years, but 2023 shows a much lower baseline, indicating the pandemic's changing phase.
Statistically, I found a significant positive correlation between cases and deaths, with a Pearson coefficient of roughly 0.64."

## 4. Code Walkthrough (3:00 - 4:00)
**Visual:** Jupyter Notebook or `src/analyze_data.py`.
**Audio:**
"Let's look at the code that generated these insights.
Here in `src/analyze_data.py`, I use Pandas 'groupby' features to aggregate daily cases into monthly totals.
I also used Scipy's `pearsonr` function here to calculate the correlation significance.
For visualization, I utilized Matplotlib to create professional-grade charts, ensuring clear labeling and grids for readability."

## 5. Conclusion (4:00 - 4:30)
**Visual:** Summary slide with key bullet points.
**Audio:**
"In conclusion, this analysis highlights the receding wave of the pandemic in early 2023 compared to previous years.
Learning to programmatically clean and analyze time-series data was a key takeaway for me.
In the future, I would like to expand this by incorporating vaccination rates to see their specific impact on the mortality curve.
Thank you for watching."
