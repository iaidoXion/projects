import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())
apiUrl = APISETTING['API']['apiUrl']
Authorization = APISETTING['API']['Authorization']
ContentType = APISETTING['API']['ContentType']
def Get(sessionKey) :
    sessionKey = sessionKey
    path = "/plugin/products/asset/v1/assets"
    urls = apiUrl + path
    headers = {
        'session' : sessionKey,
        'Authorization': Authorization,
        'Content-Type': ContentType,
    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    resCode = response.status_code
    if resCode == 200:
        systemStatus = response.text
    else :
        systemStatus = resCode

    systemStatusList = {'systemStatusList': systemStatus}
    #print(sessionKey)
    return systemStatusList

def Details(sessionKey) :
    sessionKey = sessionKey
    path = "/plugin/products/asset/v1/assetDetails"
    urls = apiUrl + path
    headers = {
        'session' : sessionKey,
        'Authorization': Authorization,
        'Content-Type': ContentType,
    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    resCode = response.status_code
    if resCode == 200:
        systemStatus = response.text
    else :
        systemStatus = resCode

    systemStatusList = {'systemStatusList': systemStatus}
    #print(sessionKey)
    return systemStatusList
