import streamlit as st
import pandas as pd
import joblib

# Load components
model = joblib.load('model/weather_classification3.pkl')
encoder = joblib.load('model/encoder.pkl')
features = joblib.load('model/features.pkl')

st.set_page_config(page_title="Weather Classifier", layout="centered")

st.title("🌦️ Weather Classification App")

# -------------------------
# Numeric Inputs
# -------------------------
temperature = st.number_input("Temperature", value=25.0)
humidity = st.number_input("Humidity", value=50.0)
wind_speed = st.number_input("Wind Speed", value=10.0)
precipitation = st.number_input("Precipitation (%)", value=20.0)
pressure = st.number_input("Atmospheric Pressure", value=1010.0)
uv = st.number_input("UV Index", value=5.0)
visibility = st.number_input("Visibility (km)", value=5.0)

# -------------------------
# Dynamic Categorical Inputs
# -------------------------
cat_features = list(encoder.feature_names_in_)   # safe
categories = encoder.categories_

cat_inputs = {}

st.markdown("### Categorical Inputs")

for i, col in enumerate(cat_features):
    cat_inputs[col] = st.selectbox(col, categories[i])

# -------------------------
# Prediction
# -------------------------
if st.button("Predict Weather"):

    # Step 1: Create input
    input_data = {
        'Temperature': temperature,
        'Humidity': humidity,
        'Wind Speed': wind_speed,
        'Precipitation (%)': precipitation,
        'Atmospheric Pressure': pressure,
        'UV Index': uv,
        'Visibility (km)': visibility
    }

    input_data.update(cat_inputs)

    input_df = pd.DataFrame([input_data])

    # Step 2: Encode categorical safely
    encoded = encoder.transform(input_df[cat_features])

    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out(cat_features)
    )

    # Step 3: Drop original categorical columns
    input_df = input_df.drop(cat_features, axis=1)

    # Step 4: Combine
    input_df = pd.concat([input_df, encoded_df], axis=1)

    # Step 5: Match training features EXACTLY
    input_df = input_df.reindex(columns=features, fill_value=0)

    # Step 6: Predict
    prediction = model.predict(input_df)[0]
    weather_map = {
    0: "☀️ Sunny",
    1: "☁️ Cloudy",
    2: "🌧️ Rainy",
    3: "❄️ Snowy"
    }


    st.success(f"🌤️ Predicted Weather: {weather_map.get(prediction, prediction)}")