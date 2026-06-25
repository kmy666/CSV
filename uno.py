import requests

API_KEY = "2P6SoRwyMPoXyddzmrzR6erv9Wdrlla2O7iVEQt6"

url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(url)
data = response.json()

print("Título:", data["title"])
print("Descripción:", data["explanation"])
print("Imagen:", data["url"])

