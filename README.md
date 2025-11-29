<<<<<<< HEAD
# citing
=======
# Electricity Consumption Predictor

This is a Streamlit app that predicts electricity consumption using a pre-trained model (`electricity_model.pkl`). The app uses `streamlit`, `pandas`, and `joblib`.

Quick local run
- Create a virtual environment (recommended):

```powershell
# Electricity Consumption Predictor

This is a Streamlit app that predicts electricity consumption using a pre-trained model (`electricity_model.pkl`). The app uses `streamlit`, `pandas`, and `joblib`.

Quick local run
- Create a virtual environment (recommended):

```powershell
python -m venv .venv
; .\.venv\Scripts\Activate.ps1
```

## Electricity Consumption Predictor

This is a Streamlit app that predicts electricity consumption using a pre-trained model (`electricity_model.pkl`). If no model file is present the app will attempt to train a fallback model from `electricity_consumption_dataset.csv`.

### Quick local run (PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

3. Run the app:

```powershell
python -m streamlit run .\app.py
```

### Deploy to Streamlit Community Cloud

1. Push your repository to GitHub (include `app.py`, `requirements.txt`, and either `electricity_model.pkl` or `electricity_consumption_dataset.csv`).
2. Open https://share.streamlit.io and sign in with GitHub.
3. Click **New app**, select your repo/branch and set the main file path to `app.py`, then click **Deploy**.

### Notes

- If `electricity_model.pkl` is large (>100 MB), store it with Git LFS or host it externally and download at runtime.
- If the app fails due to package versions, pin versions in `requirements.txt`.
- Use Streamlit Secrets for any credentials.

If you'd like, I can help push this repo to GitHub and complete the Streamlit Cloud deployment steps.
