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

    dataListAppend = []
    for i in range(0, assetsCount):
        id = assetsDataJson[i]['id']
        computer_name = assetsDataJson[i]['computer_name']
        computer_id = assetsDataJson[i]['computer_id']
        os_platform = assetsDataJson[i]['os_platform']
        operating_system = assetsDataJson[i]['operating_system']
        disk_total_space = assetsDataJson[i]['disk_total_space']
        created_at = assetsDataJson[i]['created_at']
        updated_at = assetsDataJson[i]['updated_at']
        last_seen_at = assetsDataJson[i]['last_seen_at']
        ci_installed_application = assetsDataJson[i]['ci_installed_application']
        ram = assetsDataJson[i]['ram']
        city = assetsDataJson[i]['city']
        chassis_type = assetsDataJson[i]['chassis_type']

        data = {
            'id' : id,
            'computer_name' : computer_name,
            'computer_id': computer_id,
            'os_platform': os_platform,
            'operating_system': operating_system,
            'disk_total_space': disk_total_space,
            'created_at': created_at,
            'updated_at': updated_at,
            'last_seen_at': last_seen_at,
            'asset_item' : chassis_type,
            'ci_installed_application' : ci_installed_application
        }

        dataListAppend.append(data)


        """if os_platform == 'Windows' :
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

    dataList = dataListAppend
    #print(dataList)
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
