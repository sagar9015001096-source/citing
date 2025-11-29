import streamlit as st
import pandas as pd
import joblib
import traceback
import os
import pathlib
import streamlit.components.v1 as components
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


st.set_page_config(page_title="Electricity Consumption Predictor", layout="wide")
st.title("⚡ Electricity Consumption Predictor")

# Simple navigation: choose between the Streamlit app and the static pages
PAGES = ["App (Predict)", "Home (Static)", "Dashboard (Static)", "About (Static)"]
page = st.sidebar.selectbox("Navigate", PAGES)

def render_static_page(name: str):
    # locate static HTML file and render its contents inside the Streamlit app
    base = pathlib.Path(__file__).parent / "static"
    if name == "Home (Static)":
        path = base / "index.html"
    elif name == "Dashboard (Static)":
        path = base / "dashboard.html"
    elif name == "About (Static)":
        path = base / "about.html"
    else:
        st.error("Unknown static page")
        return

    if not path.exists():
        st.error(f"Static file not found: {path}")
        return

    html = path.read_text(encoding="utf-8")
    components.html(html, height=800, scrolling=True)

if page != "App (Predict)":
    render_static_page(page)
    st.stop()

def train_and_save_model(csv_path: str, model_path: str):
    df = pd.read_csv(csv_path)
    X = df[["Temperature", "Humidity", "Appliance_Usage"]]
    y = df["Electricity_Consumption"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    score = r2_score(y_test, preds)
    joblib.dump(model, model_path)
    return model, score


model = None
model_path = "electricity_model.pkl"
if os.path.exists(model_path):
    try:
        model = joblib.load(model_path)
    except Exception:
        st.warning("Found `electricity_model.pkl` but failed to load it. Will attempt to retrain from dataset.")
        model = None

if model is None:
    csv_path = "electricity_consumption_dataset.csv"
    if os.path.exists(csv_path):
        with st.spinner("Training fallback model from `electricity_consumption_dataset.csv`..."):
            try:
                model, r2 = train_and_save_model(csv_path, model_path)
                st.success(f"Trained a fallback model (R² = {r2:.3f}) and saved to `{model_path}`.")
            except Exception:
                st.error("Failed to train a fallback model (see details).")
                with st.expander("Error details"):
                    st.text(traceback.format_exc())
                st.stop()
    else:
        st.error("No trained model found and dataset `electricity_consumption_dataset.csv` is missing.")
        st.markdown("**Options:**")
        st.markdown("- Add `electricity_model.pkl` to the project root, or")
        st.markdown("- Add `electricity_consumption_dataset.csv` so the app can train a fallback model automatically.")
        st.stop()


st.header("📥 Enter Input")

temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=30.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=60.0, step=0.1)
appliance_usage = st.number_input("Appliance Usage (kWh)", min_value=0.0, max_value=500.0, value=200.0, step=1.0)

if st.button("Predict ⚡"):
    input_data = pd.DataFrame([{
        "Temperature": temperature,
        "Humidity": humidity,
        "Appliance_Usage": appliance_usage
    }])
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"🔋 Estimated Electricity Consumption: **{prediction:.2f} units**")
    except Exception:
        st.error("Prediction failed (see details).")
        with st.expander("Error details"):
            st.text(traceback.format_exc())
