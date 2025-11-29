import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("electricity_model.pkl")

# App title
st.title("⚡ Electricity Consumption Predictor")

# User input form
st.header("📥 Enter Input ")

temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=30.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0, step=0.1)
appliance_usage = st.number_input("Appliance Usage (kWh)", min_value=0.0, max_value=500.0, value=200.0, step=1.0)

# Predict button
if st.button("Predict ⚡"):
    input_data = pd.DataFrame([{
        "Temperature": temperature,
        "Humidity": humidity,
        "Appliance_Usage": appliance_usage
    }])
    
    prediction = model.predict(input_data)[0]
    st.success(f"🔋 Estimated Electricity Consumption: **{prediction:.2f} units**")
