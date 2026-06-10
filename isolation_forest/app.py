import streamlit as st
import pandas as pd

from src.anomaly_utils import (
    load_data,
    preprocess_data,
    load_model
)

st.set_page_config(
    page_title="Isolation Forest Anomaly Detection",
    layout="wide"
)

st.title(
    "🔍 Anomaly Detection using Isolation Forest"
)

df = load_data()

st.subheader("Dataset Preview")

st.dataframe(df.head())

X = preprocess_data(df)

model = load_model()

predictions = model.predict(X)

df["Prediction"] = predictions

df["Prediction"] = df["Prediction"].replace(
    {
        1: "Normal",
        -1: "Anomaly"
    }
)

st.subheader("Prediction Results")

st.dataframe(df.head(20))

normal_count = (
    df["Prediction"] == "Normal"
).sum()

anomaly_count = (
    df["Prediction"] == "Anomaly"
).sum()

st.subheader("Distribution")

chart_data = pd.DataFrame(
    {
        "Count": [
            normal_count,
            anomaly_count
        ]
    },
    index=[
        "Normal",
        "Anomaly"
    ]
)

st.bar_chart(chart_data)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Normal Records",
        normal_count
    )

with col2:
    st.metric(
        "Anomalies Detected",
        anomaly_count
    )