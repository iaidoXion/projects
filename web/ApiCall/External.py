from urllib.parse import urlencode, unquote, quote_plus
import requests
import json

with open("setting.json", encoding="UTF-8") as f:
    APISETTING = json.loads(f.read())

serviceKey = APISETTING['API']['serviceKey']
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

def ApiModels():
    apiUrl = APISETTING['API']['apiUrl']
    dataReturnType = APISETTING['API']['dataReturnType']
    dataRows = APISETTING['API']['dataRows']
    dataPageNo = APISETTING['API']['dataPageNo']
    sidoName = APISETTING['API']['sidoName']
    ver = APISETTING['API']['ver']
    queryParams = '?' + urlencode(
        {
            quote_plus('ServiceKey'): serviceKeyDecoded,
            quote_plus('returnType'): dataReturnType,
            quote_plus('numOfRows'): dataRows,
            quote_plus('pageNo'): dataPageNo,
            quote_plus('sidoName'): sidoName,
            quote_plus('ver'): ver
        }
    )
    urls = apiUrl + queryParams
    res = requests.get(urls)
    contents = res.text
    json_ob = json.loads(contents)
    items = json_ob['response']['body']['items']

    return items