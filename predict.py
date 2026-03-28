import pandas as pd
import numpy as np
import pickle
import os

# Load model & scaler (THIS WAS MISSING ❌)
BASE_DIR = os.path.dirname(__file__)

model = pickle.load(open(os.path.join(BASE_DIR, 'kmeans_model.pkl'), 'rb'))
scaler = pickle.load(open(os.path.join(BASE_DIR, 'scaler.pkl'), 'rb'))

def predict_customer(recency, frequency, monetary):

    data = pd.DataFrame([[recency, frequency, monetary]],
                        columns=['Recency', 'Frequency', 'Monetary'])

    data_scaled = scaler.transform(data)
    cluster = model.predict(data_scaled)[0]

    # SMART LOGIC
    if recency <= 30 and frequency >= 5:
        segment = "Loyal Customer 🟢"

    elif monetary > 10000 and recency <= 30:
        segment = "High Value Customer 💎"

    elif recency > 90:
        segment = "At Risk ⚠️"

    elif frequency == 1:
        segment = "New Customer 🆕"

    else:
        segment = "Regular Customer 👤"

    return cluster, segment