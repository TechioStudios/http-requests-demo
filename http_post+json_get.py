import requests #import requests lib


form = {"username":"cloud","password":"123456"}


#send a http post request
res = requests.post('http://localhost:8000',data=form)
print(res.text)
