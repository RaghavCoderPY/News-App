import requests
import json


query = input("Search Here 🔎 ")

# Use your api key. Get your api key at https://www.newsapi.org sgin up and get it. THIS IS FREE!
API_KEY = f"https://newsapi.org/v2/everything?q={query}&apiKey=2ecfbfad7da544c2b87bb34fd0be53ed"

r = requests.get(API_KEY)
news = json.loads(r.text)

if r.status_code == 200:
    if "articles" in news:
        for article in news["articles"]:
            title = article["title"]
            desc = article["description"]
            # Printing it 
            print(f"⛳️ {title}\nMore - {desc}")
            print("-------------------------------------------------------\n")
    else:
        print("No article found")
else:
    print(f"An Error Occured Status Code {r.status_code}")
