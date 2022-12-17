import requests #import requests lib
#send a http get request
url = "https://www.starwars.com/databank/venator-class-star-destroyer"#set url
headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari 537.36"}#pretend to be web browser
tagList = ['</',"\n"," ",'"class="thumbreserved-ratio"alt="Venator-classStarDestroyer"></','class="aspect"><imgsrc="']
r = requests.get(url,headers=headers)#http get

text = r.text
img = ""

tmp = text.split('<p class="desc">')


tmp2 = tmp[1].split('</p>')
print(tmp2[0])