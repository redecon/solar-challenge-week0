# scripts/clean.py
import pandas as pd
from scipy import stats
import numpy as np

def clean_country_data(country):
    # Map raw filenames
    raw_map = {
        'benin': 'benin-malanville.csv',
        'togo': 'togo-dapaong_qc.csv',
        'sierra_leone': 'sierraleone-bumbuna.csv'  # adjust if needed
    }
    raw_file = raw_map[country]
    raw_path = f"../data/{raw_file}"
    clean_path = f"../data/{country}_clean.csv"
    
    print(f"Cleaning {country} from {raw_file}...")
    df = pd.read_csv(raw_path)
    
    # === YOUR EDA CLEANING LOGIC ===
    cols = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']
    df = df.dropna(subset=cols)  # simple for now
    # Add Z-score, imputation, etc. from your notebook
    
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df.to_csv(clean_path, index=True)
    print(f"Cleaned data saved: {clean_path}")
    return clean_path

if __name__ == "__main__":
    for c in ['benin', 'togo', 'sierra_leone']:
        clean_country_data(c)