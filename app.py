from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load('fraud_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.get("/")
def home():
    return {"message": "Fraud Detection API is running"}

@app.post("/predict")
def predict(transaction: dict):
    df = pd.DataFrame([transaction])
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]
    return {
        "fraud_prediction": int(prediction),
        "fraud_probability": float(probability)
    }