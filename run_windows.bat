@echo off
SET COINGLASS_API_KEY=%1
python -m venv .venv
call .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
streamlit run app_streamlit.py --server.maxUploadSize=200
