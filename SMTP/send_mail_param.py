#!/user/bin/env python
#encoding:utf-8

"""
读取系统参数（20170822没有运行成功，是否要重启电脑？）
"""


import smtplib
from email.utils import formataddr,parseaddr
from email.header import Header
from email.mime.text import MIMEText
import os

from_addr=os.environ(FROM_ADDR)   #环境变量参数
password=os.environ(PASSWORD)

def  _to_formatadd(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))


def  send_mail_param():
    smtp_sever=u"smtp.163.com"
    to_addr=u"18576672691@163.com"
    file=u"1.html"
    with open(file,r) as fp:
        html_data=fp.read()
    msg=MIMEText(html_data,'html','utf-8')
    msg['FROM']=_to_formatadd(u"python邮件<%s>"%from_addr)
    msg['to']=_to_formatadd(u"163y邮箱<%s>"%to_addr)
    msg['subject']=Header(u"来自Python的邮件....",'utf-8').encode()
    server=smtplib.SMTP(smtp_sever)
    server.login(from_addr,password)
    server.sendmail(to_addr,from_addr,msg.as_string())
