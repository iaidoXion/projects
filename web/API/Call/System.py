from web.API.Common.Auth import ApiAuth
import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())

def Status() :
    sessionKey = ApiAuth()
    apiUrl = APISETTING['API']['apiUrl']
    Authorization = APISETTING['API']['Authorization']
    ContentType = APISETTING['API']['ContentType']
    path = "/api/v2/system_status"
    urls = apiUrl + path
    headers = {
        'session' : sessionKey,
        'Authorization': Authorization,
        'Content-Type': ContentType,
    }

    response = requests.request("GET", urls, headers=headers, verify=False)

    print(response)

    sessionKeyList = {'sessionKey': sessionKey}
    return sessionKeyList
