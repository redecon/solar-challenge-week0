# Solar Challenge Week 0 – Solar Data Analysis  
**Multi-country solar irradiance profiling, cleaning & exploratory data analysis (EDA)**

---

## Project Overview

This repository contains a **reproducible data science pipeline** for analyzing solar radiation and weather data from **three African sites**:

- **Benin** (`benin-malanville.csv`)  
- **Togo** (`togo-dapaong_qc.csv`)  
- **Sierra Leone** (`sierraleone-bumbuna.csv`)

**Goal**: Profile, clean, and explore each dataset to prepare it for downstream modeling and regional comparison.

---

# Solar Challenge Week 0 – Multi-Country Solar Analysis  
**Profiling • Cleaning • EDA • Cross-Country Comparison • Interactive Dashboard**

---

## Project Overview

Analyze solar irradiance from **Benin**, **Togo**, and **Sierra Leone** to assess solar potential.

**Tasks**:
- Data cleaning & EDA
- Cross-country comparison
- Interactive Streamlit dashboard

---

## Repository Structure

```bash
solar-challenge-week0/
├── data/                     # Raw + cleaned CSVs (.gitignore)
├── notebooks/                # EDA + comparison
│   ├── benin_eda.ipynb
│   ├── togo_eda.ipynb
│   ├── sierraleone_eda.ipynb
│   └── compare_countries.ipynb
├── app/                      # Streamlit dashboard
│   ├── main.py
│   └── utils.py
├── .github/workflows/ci.yml  # CI/CD
├── requirements.txt
├── .gitignore
└── README.md
```
## Key Features

| Feature | Description |
|-------|-----------|
| **Virtual Environment** | `venv/` + `requirements.txt` |
| **CI/CD** | GitHub Actions runs on push/PR |
| **Outlier Removal** | Z-score > 3 → dropped |
| **Missing Value Imputation** | Median (robust) |
| **Interactive Plots** | `plotly` wind rose, `seaborn` heatmaps |
| **Cleaned Output** | `data/<country>_clean.csv` |
| **Reproducibility** | All steps in notebooks |

---

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/redecon/solar-challenge-week0.git
cd solar-challenge-week0

# 2. Create & activate virtual environment
python -m venv venv
source venv/bin/activate    # Linux/macOS
# venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Launch Jupyter
jupyter notebook

# 5. Run Dashboard
streamlit run app/main.py
```
## EDA Notebooks
Each notebook performs:

1. **Data Loading & Summary**
2. **Missing Value Report (>5% flagged)**
3. **Outlier Detection (Z-score)**
4. **Cleaning & Imputation**
5. **Time Series Plots (daily/hourly)**
6. **Cleaning Impact (ModA/ModB pre/post)**
7. **Correlation Heatmap**
8. **Scatter & Bubble Charts**
9. **Interactive Wind Rose (Plotly)**
10. **Export Cleaned CSV**

## CI/CD Pipeline
.github/workflows/ci.yml runs on:

push to main or eda-*
pull_request
### Steps:

1. **Checkout code**
2. **Setup Python 3.11**
3. **Cache pip**
4. **Install requirements.txt**
5. **Run tests (or skip)**

## Contributing

1. **Create branch: eda-<country> or feat-<name>**
2. **Commit with clear messages**
3. **Open PR → CI must pass**
4. **Merge to main**


## References

1. NASA POWER Data Access
2. Plotly Wind Rose