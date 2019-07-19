import requests
import pprint
key = 'f3f6bccf37b5643f47db688990cacfbf'
targetDt = '20190713'
api_url =  f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}'
print(api_url)
response = requests.get(api_url).json()
pprint.pprint(response)