import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained Random Forest model
model = joblib.load('fraud_rf_model.pkl')

st.title("Credit Card Fraud Detection")

st.write("Enter transaction details to check for fraud probability.")

# Input fields for features (customize as per your dataset)
time = st.number_input("Time", min_value=0.0, value=0.0)
amount = st.number_input("Amount", min_value=0.0, value=0.0)
v_features = []
for i in range(1, 29):
    v = st.number_input(f"V{i}", value=0.0)
    v_features.append(v)

if st.button("Predict Fraud Probability"):
    # Prepare input for prediction
    input_data = np.array([[time, amount] + v_features])
    # Predict probability
    proba = model.predict_proba(input_data)[0, 1]
    st.write(f"**Fraud Probability:** {proba:.4f}")
    if proba > 0.7:
        st.error("🚨 High risk of fraud!")
    elif proba > 0.3:
        st.warning("⚠️ Moderate risk of fraud.")
    else:
        st.success("✅ Low risk of fraud.")

