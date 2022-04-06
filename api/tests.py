from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup
import json
import urllib.request
serviceKey = "A3V9KkJz8Dbpgn6i4PaIGHOKNDDytz5rxrbM+QExTdCCIYVadW4FLAkEzOHGYg3QEWjBnYbF3Z6BZMLzef582A=="
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')
def check_air():
    station = []
    pm10 = []
    url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    returnType="xml"
    returnType2="json"
    numOfRows="100"
    pageNo="1"
    sidoName="대구"
    ver="1.0"

    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('returnType') : returnType, quote_plus('numOfRows') : numOfRows, quote_plus('pageNo') : pageNo, quote_plus('sidoName') : sidoName, quote_plus('ver') : ver })
    queryParams2 = '?' + urlencode({ quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('returnType') : returnType2, quote_plus('numOfRows') : numOfRows, quote_plus('pageNo') : pageNo, quote_plus('sidoName') : sidoName, quote_plus('ver') : ver })
    urls = url + queryParams2
    res = requests.get(url + queryParams)
    res2 = requests.get(urls)
    api_request = urllib.request.Request(urls)
    #movie_api_request.add_header("X-Naver-Client-Id", client_id)
    #movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(api_request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        result = json.loads(response_body.decode('utf-8'))
        items = result.get('items')
        print(items)
        print(res2)
    xml = res.text
    jsonFile = res2.text

    soup = BeautifulSoup(xml, 'html.parser')

    for tag in soup.find_all('stationname'):
        station.append(tag.text)
    for tag in soup.find_all('pm10value'):
        pm10.append(tag.text)
    res = dict(zip(station, pm10))
    print(res)
    return res