# scripts/compare.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.makedirs("../figures", exist_ok=True)  # for ranking plot

import pandas as pd
import joblib
from model import load_clean_data, prepare_features
import matplotlib.pyplot as plt

countries = ['benin', 'togo', 'sierra_leone']
results = []

for country in countries:
    df = load_clean_data(country)
    df = prepare_features(df)
    
    model = joblib.load(f"../models/{country}_ghi_model.pkl")
    X = df[model.feature_names_]
    preds = model.predict(X)
    actual = df['GHI']
    
    mae = ((preds - actual).abs()).mean()
    results.append({'Country': country.title(), 'MAE (W/m²)': round(mae, 2)})

# Ranking
results_df = pd.DataFrame(results).sort_values('MAE (W/m²)')
print("\nREGION RANKING (Lower MAE = Better)")
print(results_df)

# Plot
plt.figure(figsize=(8,5))
plt.bar(results_df['Country'], results_df['MAE (W/m²)'], color=['gold','silver','bronze'])
plt.title('Solar Prediction Accuracy by Region')
plt.ylabel('MAE (W/m²)')
plt.tight_layout()
plt.savefig("../figures/region_ranking.png")
plt.show()