import streamlit as st
import requests

st.title("Bank Fraud Detection Dashboard")
st.write("Enter transaction details to check for fraud")

amount = st.number_input("Transaction Amount", value=100.0)
time = st.number_input("Time (seconds since first transaction)", value=0.0)

v_features = {}
for i in range(1, 29):
    v_features[f"V{i}"] = st.number_input(f"V{i}", value=0.0, format="%.6f")

if st.button("Check for Fraud"):
    payload = {
        **v_features,
        "scaled_amount": amount,
        "scaled_time": time
    }
    response = requests.post("http://127.0.0.1:8000/predict", json=payload)
    result = response.json()

    if result["fraud_prediction"] == 1:
        st.error(f"⚠️ FRAUD DETECTED — Probability: {result['fraud_probability']:.2%}")
    else:
        st.success(f"✅ Transaction looks safe — Fraud Probability: {result['fraud_probability']:.2%}")