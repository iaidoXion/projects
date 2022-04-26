import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())
apiUrl = APISETTING['API']['apiUrl']
Authorization = APISETTING['API']['Authorization']
ContentType = APISETTING['API']['ContentType']

def Get(sessionKey):
    path = "/api/v2/users"
    urls = apiUrl + path
    headers = {
        'session': sessionKey,
        'Authorization': Authorization,
        'Content-Type': ContentType,

    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    resCode = response.status_code
    if resCode == 200:
        userInfo = response.text
    else :
        userInfo = resCode
    userInfoList = {'userInfoList': userInfo}
    return userInfoList


def SessionLogin(username, password) :
    path = "/api/v2/session/login"
    urls = apiUrl + path
    headers = {
        'Authorization': Authorization,
        'Content-Type': ContentType,

    }
    #authJSON = json.dumps({"username": "Administrator", "domain": "", "password": "xion123!"})
    authData = json.dumps({"username": username, "domain": "", "password": password})
    response = requests.request("POST", urls, headers=headers, data=authData, verify=False)
    resCode = response.status_code
    if resCode == 200 :
        sessionLogin = response.text
    else :
        sessionLogin = resCode
    #sessionLoginJson = json.loads(sessionLogin)
    #sessionKey = sessionLoginJson['data']['session']
    #sessionLoginList = {'sessionLoginList': {'sessionKey':sessionKey,"username":username,  "password": password }}

    return sessionLogin


def Logout(sessionKey) :
    print(sessionKey)
    # if sessionKey is not None:
        #path = "/api/v2/session/logout"
    # urls = apiUrl + path
     #  headers = {
            #'session': sessionKey,
        #            'Authorization': Authorization,
            #'Content-Type': ContentType,

        #}
        #logoutData = json.dumps({"session":sessionKey})
        #response = requests.request("POST", urls, headers=headers, data=logoutData, verify=False)
        #resCode = response.status_code
        # print(resCode)
        # if resCode == 200:
            #sessionLogout = response.text
            #    else:
    #    sessionLogout = resCode
        #sessionLoginList = {'sessionLogoutList': sessionLogout}
        #    else :
#    sessionLoginList = {'sessionLogoutList': 'session key null'}
    #return sessionLoginList