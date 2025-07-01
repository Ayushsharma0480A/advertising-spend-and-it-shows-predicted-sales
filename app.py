import streamlit as st
import numpy as np
from joblib import load

# Load the trained model
model = load('sales_model.joblib')

# Streamlit UI
st.title("📊 Sales Prediction Based on Ad Spend")
st.write("Enter your planned advertising spend to get predicted sales.")

# Input slider or number field
spend = st.number_input("Enter Ad Spend ($)", min_value=0, step=1000)

# Prediction
if spend:
    prediction = model.predict([[spend]])
    st.success(f"🛒 Predicted Sales: {int(prediction[0]):,} units")
