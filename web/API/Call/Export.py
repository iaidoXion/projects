import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())
apiUrl = APISETTING['API']['apiUrl']
Authorization = APISETTING['API']['Authorization']
ContentType = APISETTING['API']['ContentType']
def Export(sessionKey) :
    path = "/api/v2/export"
    urls = apiUrl + path
    payload = json.dumps({ "dashboards" : { "include_all" : True } })
    headers = {
        'session': sessionKey,
        'Authorization': Authorization,
        'Content-Type': ContentType,

    }

    response = requests.request("POST", urls, headers=headers, data=payload, verify=False)
    export = response.text
    print(export)
    #exportList = {'exportList': export}
    #return exportList
