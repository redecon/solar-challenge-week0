# app/utils.py
import pandas as pd
import plotly.express as px
import os
import numpy as np

DATA_PATH = "../data"

def load_data():
    files = {
        'Benin': 'benin_clean.csv',
        'Togo': 'togo_clean.csv',
        'Sierra Leone': 'sierraleone-bumbuna_clean.csv'
    }
    data = {}
    for country, file in files.items():
        path = os.path.join(DATA_PATH, file)
        if os.path.exists(path):
            df = pd.read_csv(path)
            df['Country'] = country
            data[country] = df
            print(f"Loaded {country} from {file}")
        else:
            print(f"Warning: {file} not found. Using simulated data for {country}.")
            # SIMULATED FALLBACK DATA (remove when real CSV exists)
            np.random.seed(42)
            n_samples = 10000  # Match approx size
            timestamps = pd.date_range(start='2020-01-01', periods=n_samples, freq='H')
            df_sim = pd.DataFrame({
                'Timestamp': timestamps,
                'GHI': np.random.normal(180, 50, n_samples),  # Lower mean for Sierra Leone
                'DNI': np.random.normal(150, 40, n_samples),
                'DHI': np.random.normal(100, 30, n_samples),
                'Tamb': np.random.normal(28, 5, n_samples),
                'RH': np.random.normal(75, 15, n_samples),
                'WS': np.random.normal(3, 1.5, n_samples),
                'WSgust': np.random.normal(5, 2, n_samples),
                'TModA': np.random.normal(30, 5, n_samples),
                'TModB': np.random.normal(30, 5, n_samples),
                'Cleaning': np.random.choice([0, 1], n_samples, p=[0.8, 0.2])
            })
            df_sim['Country'] = country
            data[country] = df_sim
    return data

def get_boxplot(data, countries, metric):
    df = pd.concat([data[c] for c in countries if c in data])
    fig = px.box(df, x='Country', y=metric, color='Country',
                 title=f'{metric} by Country', height=500)
    return fig

def get_summary_table(data, countries):
    dfs = []
    for c in countries:
        if c in data:
            df = data[c][['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std']).round(2)
            df['Country'] = c
            dfs.append(df)
    summary = pd.concat(dfs).set_index('Country')
    return summary