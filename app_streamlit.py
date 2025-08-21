import os
import streamlit as st
import pandas as pd
import requests
from concurrent.futures import ThreadPoolExecutor

# Initialize session state safely
if "prev_scores" not in st.session_state:
    st.session_state.prev_scores = {}

st.title("Ignition Trader — Futures Scanner")

COINGLASS_API_KEY = os.getenv("COINGLASS_API_KEY")

# Simple placeholder scanning function
def scan_symbol(symbol: str):
    # Dummy: return random score and notes
    import random, time
    score = round(random.uniform(-2, 10), 2)
    notes = "BUY" if score > 7 else ("SELL" if score < 3 else "NEUTRAL")
    metrics = {"RSI": random.randint(20, 80), "OI": random.randint(1000, 5000)}
    return {"symbol": symbol, "score": score, "signal": notes, **metrics}

symbols = ["BTCUSDT", "ETHUSDT", "XRPUSDT", "SOLUSDT"]
max_workers = st.slider("Parallel workers", 1, 20, 5)
threshold = st.slider("Signal threshold", 0.0, 10.0, 7.0)

if st.button("Run Live Scan"):
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        results = list(pool.map(scan_symbol, symbols))

    df = pd.DataFrame(results)
    df["action"] = df["score"].apply(lambda x: "BUY" if x >= threshold else "")
    st.dataframe(df)
