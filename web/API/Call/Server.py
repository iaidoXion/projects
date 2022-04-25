import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())

apiUrl = APISETTING['API']['apiUrl']
Authorization = APISETTING['API']['Authorization']

def Info(sessionKey) :
    sessionKey = sessionKey
    path = "/api/v2/server_info"
    urls = apiUrl + path
    headers = {
        'session' : sessionKey,
        'Authorization': Authorization,
    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    serverInfo = response.text

    serverInfoList = {'serverInfoList': serverInfo}
    return serverInfoList

def Host(sessionKey) :
    sessionKey = sessionKey
    path = "/api/v2/server_host"
    urls = apiUrl + path
    headers = {
        'session': sessionKey,
        'Authorization': Authorization,
    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    serverHost = response.text

    serverHostList = {'serverHostList': serverHost}
    return serverHostList
