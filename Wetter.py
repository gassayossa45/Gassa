import streamlit as st
import requests

st.title("🌤 Wetter-App mit API")

# Eingabe für Stadt-Koordinaten
latitude = st.number_input("Breitengrad", value=52.52)
longitude = st.number_input("Längengrad", value=13.41)

# API-Abfrage
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": True
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    weather = data["current_weather"]
    st.metric("🌡 Temperatur", f"{weather['temperature']} °C")
    st.metric("💨 Windgeschwindigkeit", f"{weather['windspeed']} km/h")
else:
    st.error("Fehler beim Abrufen der Wetterdaten")