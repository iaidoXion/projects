import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())
apiUrl = APISETTING['API']['apiUrl']
Authorization = APISETTING['API']['Authorization']
ContentType = APISETTING['API']['ContentType']
def Login(sessionKey) :

    path = "/api/v2/session/login"
    urls = apiUrl + path
    headers = {
        'Authorization': Authorization,
        'Content-Type': ContentType,
    }

    response = requests.request("POST", urls, headers=headers, verify=False)

    print(response.text)

    sessionKeyList = {'sessionKey': sessionKey}
    return sessionKeyList
