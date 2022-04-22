import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())

def ApiAuth():
    apiUrl = APISETTING['API']['apiUrl']
    Authorization = APISETTING['API']['Authorization']
    path = "/auth"
    urls = apiUrl+path
    headers = {
      'Authorization': Authorization
    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    session = response.text
    #print(response)
    return session
