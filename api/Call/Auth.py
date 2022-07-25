import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())
apiUrl = APISETTING['API']['apiUrl']
Authorization = APISETTING['API']['Authorization']
SesstionKeyPath = APISETTING['API']['PATH']['SesstionKey']
def SessionKey():
    try:
        path = SesstionKeyPath
        urls = apiUrl+path
        headers = {
          'Authorization': Authorization
        }
        response = requests.request("GET", urls, headers=headers, verify=False)
        resCode = response.status_code
        sessionKey = response.text
        returnList = sessionKey

        return returnList
    except ConnectionError as e:
        print(e)

