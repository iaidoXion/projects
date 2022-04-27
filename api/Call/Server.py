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
    resCode = response.status_code
    serverInfo = response.text

    dataList = serverInfo
    returnList = {'resCode': resCode, 'dataList': dataList}

    return returnList


def Host(sessionKey) :
    sessionKey = sessionKey
    path = "/api/v2/server_host"
    urls = apiUrl + path
    headers = {
        'session': sessionKey,
        'Authorization': Authorization,
    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    resCode = response.status_code
    serverHost = response.text
    dataList = serverHost
    returnList = {'resCode': resCode, 'dataList': dataList}
    return returnList