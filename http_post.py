import requests #import requests lib
#send a http post request
#r = requests.post('https://www.httpbin.org/post')
r = requests.post('localhost')
print(r.text)