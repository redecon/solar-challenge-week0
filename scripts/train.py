# scripts/train.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.makedirs("../models", exist_ok=True)
os.makedirs("../figures", exist_ok=True)

from scripts.model import load_clean_data, prepare_features, train_model, save_model, plot_feature_importance
import pandas as pd

countries = ['benin', 'togo', 'sierra_leone']

print("Starting model training...\n")

for country in countries:
    print(f"Training model for {country.upper()}...")
    
    # Load cleaned data
    df = load_clean_data(country)
    
    # Prepare features
    df = prepare_features(df)
    
    # Train
    model, mae, r2, features = train_model(df, target='GHI')
    
    # Save
    save_model(model, country)
    print(f"Model saved: models/{country}_ghi_model.pkl")
    
    # Plot importance
    plot_feature_importance(model, features, country)
    print(f"MAE: {mae:.2f} | R²: {r2:.3f}\n")

print("All models trained and saved!")