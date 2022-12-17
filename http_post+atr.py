import requests #import requests lib

#-------------------------------first way to do this
data = {
    "name":"germey",
    "age":22
}#data obj


#send a http post request
r = requests.post('http://120.79.29.218:8000',data=data)
print(r.text)