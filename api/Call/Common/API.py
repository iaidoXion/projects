import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())

apiUrl = APISETTING['API']['apiUrl']
Authorization = APISETTING['API']['Authorization']
ContentType = APISETTING['API']['ContentType']


def Auth():
    path = "/auth"
    urls = apiUrl + path
    headers = {
        'Authorization': Authorization
    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    resCode = response.status_code
    if resCode == 200:
        sessionKey = response.text
    else:
        sessionKey = resCode

    return sessionKey


def Tokens(sessionKey):
    path = "/api/v2/api_tokens"
    urls = apiUrl + path
    headers = {
        'session': sessionKey,
        'Authorization': Authorization,
        'Content-Type': ContentType,

    }
    tokensData = json.dumps({})
    response = requests.request("POST", urls, headers=headers, data=tokensData, verify=False)
    resCode = response.status_code
    if resCode == 200:
        apiTokens = response.text
    else:
        apiTokens = resCode
    apiTokensList = {'apiTokensList': apiTokens}
    return apiTokensList
