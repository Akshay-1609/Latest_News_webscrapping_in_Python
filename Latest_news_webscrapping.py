import requests 
from bs4 import BeautifulSoup
page = requests.get("https://indianexpress.com/section/india/")
soup = BeautifulSoup(page.content, 'html.parser')

title=[]
desc=[]
img=[]
count=0
for j in soup.find_all('div',{'class':'articles'}):
    for i in j.find('p'):
        desc.append(i)
    for i in j.find_all('h2'):
        for x in i.find('a'):
            title.append(x)
    for i in j.find_all('div',{'class':'snaps'}):
        for j in i.find_all('a'):
            if j.findAll('img')!=True:
                for k in j.findAll('img'):
                    img.append(k['src'])
            else:
                img.append(' ')   


leng=len(title)
final=[]
img2=[]
for i in img:
    if "trans.gif" not in i:
        img2.append(i)

for i in range(0,leng):
    a=[]
    a.append(title[i])
    a.append(desc[i])
    try:
        a.append(img2[i])
    except:
        a.append("")

    final.append(a)

for i in final:
    print(" ######", count ,"!!!!!!!!!! ")
    print("\n")
    print(i)
    count=count+1
    print("\n")


