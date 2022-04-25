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
        'session': sessionKey,
        'Authorization': Authorization,
        'Content-Type': ContentType,

    }
    authJSON = json.dumps({"username": "Administrator", "domain": "", "password": "xion123!"})
    response = requests.request("POST", urls, headers=headers, data=authJSON, verify=False)
    sessionLogin=response.text
    sessionLoginList = {'sessionLoginList': sessionLogin}
    return sessionLoginList
