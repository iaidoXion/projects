import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())
apiUrl = APISETTING['API']['apiUrl']
Authorization = APISETTING['API']['Authorization']
ContentType = APISETTING['API']['ContentType']

def Info(sessionKey) :

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

    assetText = response.text
    assetJson = json.loads(assetText)
    assetsCount = len(assetJson['data'])
    assetsDataJson = assetJson['data']




    """assetsDataKey = assetsDataJson[0].keys()
    assetsDataKeyList = []
    for i in assetsDataKey :
        assetsDataKeyList.append([i])
    print(assetsDataKeyList)"""


    """for i in range(0, assetsCount):
        id = assetsDataJson[i]['id']
        computer_name = assetsDataJson[i]['computer_name']
        os_platform = assetsDataJson[i]['os_platform']
        operating_system = assetsDataJson[i]['operating_system']
        chassis_type = assetsDataJson[i]['chassis_type']
        ram = assetsDataJson[i]['ram']
        city = assetsDataJson[i]['city']
        chassis_type = assetsDataJson[i]['chassis_type']
        if os_platform == 'Windows' :
            osPlatformWindowsCount = len(os_platform)
            print(osPlatformWindowsCount)
        
        if computer_name == 'desktop-vek69ms' :
            assets = assetsDataJson[i]
        else :
            print()

            ram = assets[i]['ram']
            city = assets[i]['city']
            print(id+':'+computer_name+':'+os_platform+':'+chassis_type+':'+operating_system+':'+ram)
        """
    dataList = assetJson
    returnList = {'resCode': resCode, 'dataList': dataList}

    return returnList


def Attributes(sessionKey) :
    sessionKey = sessionKey
    path = "/plugin/products/asset/v1/attributes"
    urls = apiUrl + path
    headers = {
        'session': sessionKey,
        'Authorization': Authorization,
        'Content-Type': ContentType,
    }
    response = requests.request("GET", urls, headers=headers, verify=False)
    resCode = response.status_code
    AttributesText = response.text
    #print(AttributesText)
    dataList = AttributesText

    returnList = {'resCode':resCode, 'dataList': dataList}

    return returnList



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

    dataList = response.text
    returnList = {'resCode':resCode, 'dataList': dataList}
    #print(sessionKey)
    return returnList
