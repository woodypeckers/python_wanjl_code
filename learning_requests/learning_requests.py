#!/user/bin/env python
#encoding:utf-8



import requests,json
import urllib
from urlparse import  urlparse
from urlparse import  urlunparse
import  os

url = 'http://202.105.139.117:8888/PDDM/index.jsp'







def learning_requests():

    data1=requests.get(url)
    print data1.status_code
    print data1.text
    print data1.cookies
    print data1.headers
    files={'file':open('1.txt','r')}
    url2='http://httpbin.org/post'
    data2=requests.post(url2,files=files)   #???
    data2=requests.post(url2,file=files)   #???

    #data2=requests.post(url,files=files)   #???

    print data2.text
    print data2.content


def learning_urlib():
    data3=urllib.urlopen(url)
    print data3
    #data4=data3.readlines()
    data4=data3.read()
    print data4
    filename,header=urllib.urlretrieve(url,'1.html')
    print filename,header
    param='shenzheng'
    dict={"age":18,"name":"zhangsan"}
    print urllib.quote(url+param)
    print urllib.quote_plus(url+param)
    print urllib.urlencode(dict)


def learning_urlparse():
    data6=urlparse(url)
    data7=data6.netloc.split('.')[0]
    print data6,data7
    data8=urlunparse(data6)
    print data8
    print os.path.splitext(data6.path)

if __name__== '__main__':

    learning_requests()
    #learning_urlib()
    #learning_urlparse()


