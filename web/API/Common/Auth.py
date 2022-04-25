import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())
apiUrl = APISETTING['API']['apiUrl']
Authorization = APISETTING['API']['Authorization']
def ApiAuth():
    path = "/auth"
    urls = apiUrl+path
    headers = {
      'Authorization': Authorization
    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    sessionKey = response.text
    return sessionKey
