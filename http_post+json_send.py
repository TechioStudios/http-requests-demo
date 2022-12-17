import requests #import requests lib
import json


form = {"username":"cloud","password":"123456"}


#send a http post request
res = requests.post('https://localhost:8000',data=json.dumps(form), verify=False)
print(res.text)
