import requests
import streamlit as sl


headers = {
    "User-Agent":"Mint News",
    "Accept": "application/json"
}

API_KEY = sl.secrets["NEWS_API_KEY"]
response = requests.get(f"https://newsapi.org/v2/everything?q=bitcoin&apiKey={API_KEY}",headers=headers)
data = response.json()

sl.title("Welcome to Mint news!")
articles = data["articles"]
for article in articles:
    sl.subheader(article["title"])
    if article["urlToImage"]:
        sl.image(article["urlToImage"])
    sl.write(article["description"])
    sl.write(f"Read more {article["url"]}")
    sl.write("Thanks!")


