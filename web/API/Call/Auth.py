import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())
apiUrl = APISETTING['API']['apiUrl']
Authorization = APISETTING['API']['Authorization']
def SessionAuth():
    path = "/auth"
    urls = apiUrl+path
    headers = {
      'Authorization': Authorization
    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    resCode = response.status_code
    if resCode == 200:
        sessionKey = response.text
    else :
        sessionKey = resCode

    return sessionKey