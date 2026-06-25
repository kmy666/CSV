import streamlit as st
import pandas as pd
import requests

API_KEY = "2P6SoRwyMPoXyddzmrzR6erv9Wdrlla2O7iVEQt6"

url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(url)
data = response.json()

df = pd.DataFrame([{
    "titulo": data["title"],
    "fecha": data["date"],
    "explicacion": data["explanation"]
}])

st.title("NASA API")

st.dataframe(df)

st.image(data["url"])
