import requests
import json

# WARNING: Use your api if you want to create using my news app
r = requests.get("https://newsapi.org/v2/everything?q=keyword&apiKey=2ecfbfad7da544c2b87bb34fd0be53ed")
# loads all the text
data = json.loads(r.text)
# checking status code
if r.status_code == 200:
    # if articles in data
    if "articles" in data:
        # user input for article number
        try:
            num = int(input("Which article no. you want: "))
            # article
            article = data["articles"][num]
            # title and description of the article
            title = article.get("title")
            desc = article.get("description")
            # printing it 
            print(f"{title}\nMore: {desc}")
        except ValueError:
            print("Only numbers are allowed")
    else:
        print("No article found")
else:
    print(f"Sorry this is an error: {r.status_code}")