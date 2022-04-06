import requests

url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth'
params ={
	'serviceKey' : 'A3V9KkJz8Dbpgn6i4PaIGHOKNDDytz5rxrbM+QExTdCCIYVadW4FLAkEzOHGYg3QEWjBnYbF3Z6BZMLzef582A==',
	'returnType' : 'json',
	'numOfRows' : '100',
	'pageNo' : '1',
	'sidoName' : '서울',
	'ver' : '1.0'
}

response = requests.get(url, params=params)
print(response.content)