from urllib.parse import urlencode, unquote, quote_plus
import requests
import json

serviceKey = "A3V9KkJz8Dbpgn6i4PaIGHOKNDDytz5rxrbM+QExTdCCIYVadW4FLAkEzOHGYg3QEWjBnYbF3Z6BZMLzef582A=="
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

def ApiModels():
    apiUrl = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    dataReturnType = "json"
    dataRows = "100"
    dataPageNo = "1"
    sidoName = "대구"
    ver = "1.0"
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