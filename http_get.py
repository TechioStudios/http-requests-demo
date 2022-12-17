import requests #import requests lib
#send a http get request
r = requests.get('https://www.httpbin.org/get')
#response type
print(type(r))
#reponse status code
print(r.status_code)
#reponse text type
print(type(r.text))
#reponse text
print(r.text)
#response cookies
print(r.cookies)