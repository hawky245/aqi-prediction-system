"""
AQI Prediction System

Author: Abhay Surya R

Predicts future Air Quality Index values using
Linear Regression and historical AQI data.
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("YOUR CSV NAME")

df = df.dropna(subset=["date", "aqi_value"])

df["date"] = pd.to_datetime(df["date"])

df["day"] = df["date"].dt.day
df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year

X = df[["day", "month", "year"]]

y = df["aqi_value"]

model = LinearRegression()

model.fit(X, y)

st.set_page_config(page_title="AQI Predictor", layout="centered")

st.title("Future AQI Prediction")

day = st.number_input("Enter Day", 1, 31, 1)
month = st.number_input("Enter Month", 1, 12, 1)
year = st.number_input("Enter Year", 2025, 2035, 2026)

if st.button("Predict AQI"):

    future_data = pd.DataFrame({
        "day": [day],
        "month": [month],
        "year": [year]
    })

    prediction = model.predict(future_data)

    predicted_aqi = prediction[0]

    st.subheader(f"Predicted AQI: {predicted_aqi:.2f}")

    future_days = [1, 5, 10, 15, 20]

    future_predictions = []

    for d in future_days:

        temp_data = pd.DataFrame({
            "day": [d],
            "month": [month],
            "year": [year]
        })

        pred = model.predict(temp_data)

        future_predictions.append(pred[0])

    fig, ax = plt.subplots()

    ax.plot(future_days, future_predictions, marker='o')

    ax.set_xlabel("Day")
    ax.set_ylabel("Predicted AQI")
    ax.set_title("Future AQI Forecast")

    st.pyplot(fig)

    if predicted_aqi <= 50:
        st.success("🟢 Good")

    elif predicted_aqi <= 100:
        st.warning("🟡 Moderate")

    elif predicted_aqi <= 200:
        st.warning("🟠 Poor")

    else:
        st.error("🔴 Severe")
