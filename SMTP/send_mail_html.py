#!/user/bin/env  python
#encoding:utf-8

"""
发送简单的HTML邮件
邮箱是163邮箱
用户：18576672691@163.com
第三方授权码：vein18576672691
"""

import  smtplib
from email.utils import formataddr,parseaddr
from email.header import Header
from email.mime.text import MIMEText

def  _to_formataddr(s):

    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr)) #一个参量

def  send_mail_html():

    from_addr=u'18576672691@163.com'
    to_addr=u'18576672691@163.com'
    smtp_server=u'smtp.163.com'
    password=u'vein18576672691'

    file=u'1.html'


    with  open(file,'r') as fp:
        html_data=fp.read()

    msg=MIMEText(html_data,'html','utf-8')  #显示HTML里面的内容
    #msg=MIMEText(html_data,'plain','utf-8')  #显示整个HTML的全部内容

    msg['from']=_to_formataddr(u"ppdm平台<%s>"%from_addr)
    msg['to']=_to_formataddr(u"邮件系统<%s>"%to_addr)
    msg['header']=Header(u"邮件",'utf-8').encode()
    server=smtplib.SMTP(smtp_server)
    server.login(from_addr,password)
    server.sendmail(from_addr,to_addr,msg.as_string())
    server.quit()



