# Zomato Restaurant & Customer Insights Analysis

**An Interactive Data Analytics and Business Intelligence Dashboard**

**Author:** Chetan Chaudhari  
**Project Type:** Data Analytics Internship Project

---

## Overview

This project performs a complete end-to-end data analytics workflow on the Zomato restaurant dataset. It covers data cleaning, exploratory data analysis, feature engineering, statistical analysis, automated business insights, and an interactive Streamlit dashboard. All findings are calculated directly from the real dataset — no values are fabricated.

---

## Problem Statement

Raw restaurant listing data contains valuable but unstructured information about cuisines, pricing, ratings, customer engagement, and service availability. Without structured analysis, these signals remain invisible. This project converts the raw Zomato dataset into clear, data-driven business insights.

---

## Objectives

- Understand restaurant distribution across cities and localities
- Identify the most popular cuisines
- Analyse restaurant ratings and customer votes
- Understand pricing patterns and cost distribution
- Measure online delivery and table booking adoption
- Discover relationships between price, rating, votes, and services
- Generate automated business insights from calculated metrics
- Build an interactive dashboard for stakeholder exploration

---

## Dataset

| Property | Value |
|---|---|
| File | `zomato.csv` |
| Rows | 9,551 |
| Columns | 21 |
| Missing values | 9 (Cuisines column only) |
| Duplicate rows | 0 |
| After cleaning | 9,542 rows, 18 columns |

**Key columns:** Restaurant ID, Restaurant Name, Country Code, City, Locality, Cuisines, Average Cost for two, Currency, Has Table booking, Has Online delivery, Price range, Aggregate rating, Rating text, Votes

---

## Dataset Source

The dataset was provided as part of the Data Analytics Internship project. It is a standard Zomato restaurant dataset widely used for academic analytics exercises. If you need to obtain a copy, search for "Zomato Restaurants Dataset" on public data portals such as Kaggle.

---

## Technologies

| Category | Tools |
|---|---|
| Language | Python 3.x |
| Data Manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Dashboard | Streamlit |
| Notebook | Jupyter |
| Report | python-docx |
| Serialization | nbformat, openpyxl |

---

## Project Architecture

```
Zomato_Analytics_Project/
|
+-- data/
|   +-- raw/
|   |   +-- zomato.csv                  (original dataset)
|   +-- cleaned/
|       +-- zomato_cleaned.csv          (cleaned + engineered dataset)
|
+-- notebooks/
|   +-- Chetan_Chaudhari_Zomato_Restaurant_Analytics.ipynb
|
+-- src/
|   +-- data_cleaning.py               (load, clean, engineer features)
|   +-- analysis.py                    (all analysis functions)
|   +-- insights.py                    (automated insight engine)
|
+-- app/
|   +-- streamlit_app.py               (interactive dashboard)
|
+-- visualizations/
|   +-- 01_restaurants_by_city.png     (and 12 more charts)
|
+-- report/
|   +-- Chetan_Chaudhari_Zomato_ProjectReport.docx
|
+-- Chetan_Chaudhari_Zomato_Analysis.py  (main pipeline script)
+-- requirements.txt
+-- README.md
```

---

## Folder Structure

```
Zomato_Analytics_Project/
├── data/raw/zomato.csv
├── data/cleaned/zomato_cleaned.csv
├── notebooks/Chetan_Chaudhari_Zomato_Restaurant_Analytics.ipynb
├── src/data_cleaning.py
├── src/analysis.py
├── src/insights.py
├── app/streamlit_app.py
├── visualizations/  (13 PNG charts)
├── report/Chetan_Chaudhari_Zomato_ProjectReport.docx
├── Chetan_Chaudhari_Zomato_Analysis.py
├── requirements.txt
└── README.md
```

---

## Installation

```bash
# 1. Clone or download the project folder
# 2. Navigate to the project directory
cd Zomato_Analytics_Project

# 3. Install required packages
pip install -r requirements.txt
```

---

## Requirements

```
pandas
numpy
matplotlib
seaborn
plotly
streamlit
jupyter
openpyxl
python-docx
nbformat
```

---

## Running the Jupyter Notebook

```bash
# From the project root
jupyter notebook notebooks/Chetan_Chaudhari_Zomato_Restaurant_Analytics.ipynb
```

Run all cells from top to bottom. The notebook is self-contained and explains every step.

---

## Running the Python Script

```bash
# From the project root
python Chetan_Chaudhari_Zomato_Analysis.py
```

This will:
- Load and profile the raw dataset
- Clean the data
- Engineer new features
- Save `data/cleaned/zomato_cleaned.csv`
- Generate and save 13 chart images to `visualizations/`
- Print statistical analysis and automated insights

---

## Running the Streamlit Dashboard

```bash
# From the project root
streamlit run app/streamlit_app.py
```

The dashboard will open at `http://localhost:8501` in your browser.

---

## Dashboard Features

The interactive dashboard contains **9 sections** accessible as tabs:

| Tab | Content |
|---|---|
| Executive Overview | KPI cards, rating/city/price distribution |
| Restaurant Analysis | Top restaurants by votes & rating, city distribution |
| Customer & Rating | Rating histogram, votes scatter, hidden gems |
| Cuisine Analysis | Top cuisines, average rating by cuisine |
| Location Analysis | City comparisons, delivery by city |
| Pricing Analysis | Price distribution, box plots, cost by category |
| Services Analysis | Delivery & booking adoption, rating by service |
| Automated Insights | 12 auto-generated business insights |
| Data Explorer | Searchable, filterable, downloadable table |

### Sidebar Filters
- City (multi-select)
- Cuisine (multi-select)
- Price Category (multi-select)
- Rating range (slider)
- Online Delivery (checkbox)
- Table Booking (checkbox)
- Reset Filters button

All charts and KPIs respond to sidebar filters.

---

## Data Cleaning

| Step | Action | Rows Affected |
|---|---|---|
| Missing Cuisines | Dropped 9 rows | -9 |
| Whitespace | Stripped from all string columns | All |
| Yes/No flags | Converted to 1/0 | Has Table booking, Has Online delivery |
| Numeric types | Ensured correct dtypes | Cost, Rating, Votes, Price range |
| Unused columns | Dropped 3 columns | Locality Verbose, Is delivering now, Switch to order menu |
| Final shape | 9,542 rows x 18 columns | — |

---

## EDA

**Key findings from the actual dataset:**

- **9,542** restaurants across **140** cities
- **145** unique individual cuisines
- **57.4%** of restaurants are in New Delhi
- **22.5%** of restaurants are unrated (Aggregate rating = 0)
- Average rating (rated only): **3.44 / 5.0**
- **North Indian** is the most common cuisine (3,960 restaurants)
- **25.7%** offer online delivery; **12.1%** offer table booking
- Luxury restaurants have an average rating of **3.89** vs **3.24** for Budget
- Pearson r (Rating vs Votes): **0.31** — moderate positive correlation

---

## Automated Insights

The `src/insights.py` module generates 12 automated business insights by calculating real metrics and building human-readable findings. Each insight includes:

1. A **metric** (calculated number from the dataset)
2. A **finding** (what the data shows)
3. An **interpretation** (business meaning)
4. A **recommendation** (suggested action)

---

## Key Findings

1. New Delhi holds 57.4% of all listed restaurants
2. North Indian cuisine leads with 3,960 restaurants
3. 22.5% of restaurants have no customer rating
4. Premium/Luxury restaurants rate higher than Budget on average
5. Online delivery and table booking are both minority features (<30%)
6. Votes and ratings have a moderate positive correlation (r=0.31)
7. Mid-Range restaurants show higher delivery adoption than Budget (41.3% vs 15.8%)
8. Table booking restaurants average a higher rating than non-booking ones (3.59 vs 3.41)

---

## Business Recommendations

> Note: These are data-informed suggestions, not guarantees.

1. **Expand delivery** in Budget and Premium segments where adoption is below average
2. **Target unrated restaurants** with first-review campaigns to improve platform quality
3. **Diversify cuisine offerings** in cities dominated by North Indian cuisine
4. **Enable table booking** for premium establishments to attract planned diners
5. **Explore Tier-2 cities** where competition is lower and restaurant density is growing

---

## Limitations

- The dataset is predominantly India-centric (90.6% India)
- Cost values are in mixed currencies across countries
- Rating of 0 means "Not Rated", not actually 0/5
- The dataset is a snapshot in time — trends over time cannot be analysed
- Restaurant names may have minor encoding inconsistencies

---

## Future Scope

- Add time-series analysis if historical data becomes available
- Build a restaurant recommendation engine
- Add NLP sentiment analysis on review text
- Expand to real-time data via Zomato API
- Train ML models to predict restaurant ratings

---

## Author

**Chetan Chaudhari**  
Data Analytics Internship Project

---

*All statistics in this README are calculated from the actual uploaded dataset.*
