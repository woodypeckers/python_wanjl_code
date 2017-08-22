#!/user/bin/env python
#encoding:utf-8

"""
邮件中带附件
QQ邮箱发给163邮箱
邮件中敏感词汇会发往垃圾箱中
"""

import smtplib
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.header import Header
from  email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def  _to_formataddr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))



def send_mail_attchment():
    smtp_servr=u'smtp.qq.com'
    from_addr=u'987184308@qq.com'
    password=u'fhhavijikdiibfdj'

    to_addr=u'18576672691@163.com'

    msg=MIMEMultipart()
    msg['from']=_to_formataddr(u"qq邮箱<%s>" % from_addr)
    msg['to']=_to_formataddr(u"163邮箱<%s>"% to_addr)
    msg['subject']=Header(u"来自QQ的一封邮件",'utf-8').encode()
    msg.attach(MIMEText(u"来自QQ的一封邮件，附件见详情。。。",'plain','utf-8'))

    file=u"1.html"
    with open(file,'rb') as fp:
        mime=MIMEBase('html','html',filename=file) #设置附件的MIME和文件名，这里是html类型:
        #mime.add_header(u'dimso','dfie',filename=file)  # 加上必要的头信息:
        mime.set_payload(fp.read())  # 把附件的内容读进来:
        #encoders.encode_base64(mime)   #用Base64编码
        msg.attach(mime)  # 添加到MIMEMultipart



    server=smtplib.SMTP_SSL(smtp_servr,465)  #smtp_ssl安全机制
    server.login(from_addr,password)
    server.sendmail(from_addr,to_addr,msg.as_string())
    server.quit()

