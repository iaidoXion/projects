import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())
apiUrl = APISETTING['API']['apiUrl']
Authorization = APISETTING['API']['Authorization']
ContentType = APISETTING['API']['ContentType']

def Status(sessionKey) :
    sessionKey = sessionKey
    path = "/api/v2/system_status"
    urls = apiUrl + path
    headers = {
        'session' : sessionKey,
        'Authorization': Authorization,
        'Content-Type': ContentType,
    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    resCode = response.status_code
    systemStatus = response.text
    dataList = systemStatus
    returnList = {'resCode': resCode, 'dataList': dataList}
    return returnList
