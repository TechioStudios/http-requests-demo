from urllib import response
import requests
import xlwt

url = "http://tool.lu/school/index.html"#set url
headers = {"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari 537.36"}#pretend to be web browser
res = requests.get(url,headers=headers)#http get

text = res.text#save response
college_info = []
tmp=[]
tagList = ["\n"," ","</td>",'<span style="color: #009A61;">','</span>',"<tr>","</tr>",\
"<p>注：<p>",'<ht width="20%">',"</th>",'<span style="color:#E74C3C;">','</table>',\
"<p>注：</p>",'<spanstyle="color:#009A61;">','<spanstyle="color:#E74C3C;">']


text_list = text.split('<table width="100%" cellspacing="0" cellpadding="0" class="tbl">')#split by "table" tag
college_list = text_list[1].split("<tr>")
for i in college_list:
    for e in tagList:
        i = i.replace(e,"")
    college_info.append(i.split("<td>"))

del college_info[0]

college_info[0] = ['','学校名称','985','211','双一流']
for i in college_info:
    del i[0]
    tmp.append(i)
del college_info[0]
college_info = tmp
# for i in college_info:
#     print(i)


book = xlwt.Workbook()
table = book.add_sheet("1")

info_len = len(college_info)
for i in range(info_len):
    for j in range(4):
        table.write(i,j,college_info[i][j])#args:target Row,target Line,data

book.save("./test.xls")