# scripts/model.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

def load_clean_data(country):
    path = f"../data/{country}_clean.csv"
    df = pd.read_csv(path, index_col='Timestamp', parse_dates=True)
    return df

def prepare_features(df):
    df = df.copy()
    df['hour'] = df.index.hour
    df['month'] = df.index.month
    df['dayofyear'] = df.index.dayofyear
    df['is_day'] = ((df.index.hour >= 6) & (df.index.hour <= 18)).astype(int)
    return df

def train_model(df, target='GHI'):
    features = ['DNI', 'DHI', 'Tamb', 'RH', 'WS', 'hour', 'month', 'dayofyear', 'is_day']
    X = df[features]
    y = df[target]
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    preds = model.predict(X)
    mae = mean_absolute_error(y, preds)
    r2 = r2_score(y, preds)
    
    return model, mae, r2, X.columns

def save_model(model, country):
    joblib.dump(model, f"../models/{country}_ghi_model.pkl")

def plot_feature_importance(model, features, country):
    plt.figure(figsize=(10,6))
    importances = model.feature_importances_
    idx = np.argsort(importances)[::-1]
    sns.barplot(x=importances[idx], y=np.array(features)[idx])
    plt.title(f'Feature Importance - {country}')
    plt.tight_layout()
    plt.savefig(f"../figures/{country}_importance.png")
    plt.show()