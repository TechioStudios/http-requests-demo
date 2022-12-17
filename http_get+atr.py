import requests #import requests lib

#-------------------------------first way to do this
data = {
    "name":"germey",
    "age":22
}#data obj


#send a http get request
r = requests.get('https://www.httpbin.org/get',params=data)
print(r.text)


#-------------------------------second way to do this
r = requests.get('https://www.httpbin.org/get?name=germey&age=20')
print(r.text)