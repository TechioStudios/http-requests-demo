import requests #import requests lib
#send a http get request
res = requests.get('https://www.httpbin.org/get')
print(res.json())