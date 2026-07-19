# 🌦️ India Historical Weather Analytics: Climate Intelligence Dashboard

## 📌 Project Overview
An advanced **Climate Intelligence Dashboard** built for deep exploratory analysis, feature engineering, and statistical anomaly tracking of historical weather patterns in India. 

Leveraging an extensive dataset of **91,320 daily records** across **10 major Indian urban centers** over 25 continuous years (**2000–2024**), this application transforms raw daily climate readings into structured, actionable insights. Built with **Python, Pandas, and Streamlit**, it enables users to instantly analyze data variance, spot extreme distributions, and extract clean data slices.

---

## 📊 Key Metrics at a Glance
| Metric | Value |
| :--- | :--- |
| 👥 Total Observations | 91,320 Rows |
| 🏙️ Target Coverage | 10 Major Indian Cities |
| 📅 Temporal Range | 2000–2024 (25 Years) |
| 📄 Total Features | 22 Columns (Raw & Derived) |
| 🌡️ Absolute Hottest | 46.4°C (Delhi & Ahmedabad, May 2024) |
| ❄️ Absolute Coldest | 7.0°C (Lucknow, February 2008) |
| 🌧️ Extreme Precipitation Peak | 339.9 mm (Ahmedabad, July 2017) |
| ⚙️ ETL Integrity | 100% Preprocessing Complete |

---

## 🚀 Core Features

### 📂 Automated ETL Pipeline & Feature Engineering
* **Data Preprocessing:** Automated script to eliminate duplicates, handle missing signatures, enforce strict date formatting `(YYYY-MM-DD)`, and optimize column data types.
* **Meteorological Season Mapping:** Algorithmic categorization of calendar dates into standard Indian weather cycles (Winter, Summer, Monsoon, Post-Monsoon).
* **Derived Metrics & Flags:** Programmatic computation of dynamic *Temperature Ranges* and automated boolean flags for *Heatwaves* and *Heavy Rain* events.

### 📈 Statistical Visualizations & Insight Automation
* **Distribution Mechanics:** Cohesive multi-city stacked histograms aligned with horizontal box plots for precise outlier tracking ($Q3 + 1.5 \times IQR$).
* **Reactive Time-Series:** 30-day moving averages (`.rolling().mean()`) driven by responsive user timeline sliders.
* **Automatic Insights & Export Engine:** Dynamic backend scripts evaluate user filters to generate instantaneous textual takeaways, paired with an encoded server-side file stream to download customized data subsets directly as CSVs.

---

## 📁 Project Modules & Architecture
| Module | Description |
| :--- | :--- |
| **Data Engineering** | Handles duplicate removal, missing data validation, and categorical mapping. |
| **Overview Page** | Renders high-level executive cards, structural summary metrics, and spatial footprints. |
| **City Explorer** | Houses micro-level trends, rolling average metrics, and historic peaks. |
| **City Comparison** | Compares regional footprints using multi-axis radar plots and seasonal variance bars. |
| **Weather Extremes** | Renders data distribution profiles, outlier box plots, and ranking leaderboards. |


## 🛠️ Tools & Technologies
* **Language & Core Libraries:** Python, Pandas, NumPy
* **Interface & Deployment:** Streamlit (Multi-page state architecture)
* **Graphics & Visualization:** Plotly Interactive Engine (Histograms, Box plots, Radar charts)
* **Workspace:** VS Code, Git

---

## 💡 Key Historical Insights
* 📌 **Northern cities** exhibit substantially wider seasonal variation amplitudes than southern regions.
* 📌 **Thermal Peaks** reached historical maximums in May, with **Delhi** and **Ahmedabad** topping thresholds at **46.4°C**.
* 📌 **Mumbai** dominates the annual rainfall distribution footprint, maintaining the highest frequency of heavy precipitation cycles.
* 📌 **Precipitation Flashpoints** reveal heavy cloudburst anomalies, peaked by an intense **339.9 mm** single-day rainfall in **Ahmedabad**.

---

## ⚠️ Limitations & Strategic Future Scope
> **Scope Boundary:** This platform functions as a historical descriptive and diagnostic application.

### Current Limitations
* ❌ **Static Data:** Runs on historical files (2000–2024); lacks active live-weather API webhooks.
* ❌ **Descriptive Bounds:** Focused on analytical data parsing; lacks machine learning forecasting engines.
* ❌ **Geographic Constraints:** Structural boundaries are strictly limited to the 10 target urban cities.
* ❌ **Visual Scope:** Built around statistical charts; completely lacks integrated geospatial GIS mapping layers.



### 🚀  Future Scope 
* ⚡ **Live Weather API Integration:** 
* 🧠 **Weather Forecasting:** 
* 🔮 **Climate Anomaly Prediction:** 
* 🗺️ **Interactive GIS Maps:**
* 🚨 **Early Warning Matrix:** 
* 🍃 **AQI Tracking:** 
* 📄 **PDF Automated Reporting:** 
* 🤖 **AI Weather Assistant:** 