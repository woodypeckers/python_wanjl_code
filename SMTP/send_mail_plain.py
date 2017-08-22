#!/user/bin/env python
#encoding:utf-8


"""
发送简单的文本邮件
邮箱是163邮箱
用户名：m18576672691@163.com
密码；18576672691Wjl
第三方授权码：vein18576672691

"""

import  smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr




def send_mail_plain():

    smtp_sever=u"smtp.163.com"
    #smtp_user=u'm18576672691@163.com'
    smtp_password=u'vein18576672691'
    from_addr=u"18576672691@163.com"
    #to_addrs=(u'18576672691@163.com', u'987184308@qq.com')
    to_addr=u'18576672691@163.com'

    msg=MIMEText("SEND EMAIL",'plain', 'utf-8')
    server=smtplib.SMTP(smtp_sever)
    server.login(from_addr,smtp_password)
    server.set_debuglevel(2)
    server.sendmail(from_addr,to_addr,msg.as_string())   #msg.as_string（）方法很重要
    server.quit()

