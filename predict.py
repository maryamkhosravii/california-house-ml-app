import joblib
import pandas as pd


model = joblib.load ("best_model.pkl")

def predict_price (data:dict):
    df = pd.DataFrame([data])
    return {model.predict(df)[0]}