import requests
import json

def ApiModels():
    apiUrl = "http://localhost:8000/api/menuList/"
    urls = apiUrl
    res = requests.get(urls)
    print(res)
    contents = res.text
    json_ob = json.loads(contents)

    items = json_ob['response']['body']

    return items