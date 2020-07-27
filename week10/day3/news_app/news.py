import requests

api_key = '35f754e21cb449b79e2be6dac7e5fb82'
endpoint = 'https://newsapi.org/v2/top-headlines?'

payload = {
    "country": "us"
}
r = requests.get(endpoint, params={'apiKey' : api_key, "country" : payload["country"],})

def get_news(api, param):
    r = requests.get(endpoint, params={'apiKey': api_key, "country": payload["country"],})
    print(r.text)


get_news(api_key, payload)


#news_elements -> sets up variables to auto populate html (title, picture, etc)

