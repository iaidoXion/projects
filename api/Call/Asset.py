import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())
apiUrl = APISETTING['API']['apiUrl']
Authorization = APISETTING['API']['Authorization']
ContentType = APISETTING['API']['ContentType']

def AssetGet(sessionKey) :
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
        assetText = response.text
        assetJson = json.loads(assetText)
        assetsCount = len(assetJson['data'])
        assetsDataJson = assetJson['data']
        assetsDataJsonList = assetsDataJson[0].keys()
        assets1 = assetJson['data'][0]
        #print(assets1)



        for i in range(0, assetsCount):
            id = assetsDataJson[i]['id']
            computer_name = assetsDataJson[i]['computer_name']
            os_platform = assetsDataJson[i]['os_platform']
            chassis_type = assetsDataJson[i]['chassis_type']
            ram = assetsDataJson[i]['ram']
            city = assetsDataJson[i]['city']
            if computer_name == 'desktop-vek69ms' :
                assets = assetsDataJson[i]
            else :
                print()

        #    ram = assets[i]['ram']
        #    city = assets[i]['city']
        #    print(id+':'+computer_name+':'+os_platform+':'+chassis_type+':'+operating_system+':'+ram)


    else :
        assets = resCode

    assetList = {'assetList': assetsDataJsonList}

    return assetList

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
