# Electricity Consumption Predictor

This repository contains a Streamlit app that predicts electricity consumption. The app will either load a pre-trained model (`electricity_model.pkl`) from the project root or will train a fallback Random Forest model from `electricity_consumption_dataset.csv`.

Repository contents (important files)

- `app.py` — Streamlit application (prediction UI). You can also view static pages inside the Streamlit app via the sidebar.
- `electricity_consumption_dataset.csv` — small sample dataset used to train a fallback model if no pre-trained model is present.
- `electricity_model.pkl` — optional pre-trained model (not included by default).
- `requirements.txt` — Python dependencies.
- `static/` — lightweight static site with `index.html`, `dashboard.html`, `about.html`, and `css/styles.css`.

Quick local run (PowerShell)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

3. Run the Streamlit app:

```powershell
python -m streamlit run .\app.py
```

Preview the static pages locally

You can preview the static pages in your browser or serve them with a simple HTTP server:

```powershell
# from the repository root
python -m http.server 8000 -d static
# open http://localhost:8000/index.html
```

Embedding static pages in Streamlit

The Streamlit app includes a sidebar navigation that can render the static pages directly inside the app (no external hosting required). Choose "Home (Static)", "Dashboard (Static)", or "About (Static)" from the sidebar.

Deploy to Streamlit Community Cloud

1. Push your repository to GitHub (ensure `app.py`, `requirements.txt`, and either `electricity_model.pkl` or the dataset are present).
2. Open https://share.streamlit.io and sign in with GitHub.
3. Click **New app**, select your repository and branch (usually `main`), and set the main file path to `app.py`.
4. Click **Deploy**. Streamlit will install packages from `requirements.txt` and start the app.

Troubleshooting & tips

- If the app fails because a package is missing or the wrong version is installed, pin package versions in `requirements.txt` and redeploy.
- If your model file is larger than GitHub's recommended sizes (>100 MB), use Git LFS or host the model externally (S3/GCS) and modify `app.py` to download it at startup.
- Check the Streamlit app logs (App → Manage app → Logs) for runtime tracebacks; share the logs and I can help fix issues.

If you'd like, I can complete the remaining steps for you:

- (A) Integrate or style the static pages further and embed charts into the dashboard.
- (B) Walk you through creating the Streamlit Cloud app and monitor the first deploy logs.
- (C) Add a small script to download a hosted model and wire it into `app.py`.
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
