#!/user/bin/env python
#encoding:utf-8

"""
main()里调用smtp的各种场景用例
"""


from  send_mail_plain  import  send_mail_plain
from  send_mail_html  import  send_mail_html
#from  send_mail_param import send_mail_param
from  send_mail_attachment import send_mail_attchment
if __name__=="__main__":
    #send_mail_plain()
    #send_mail_html()
    #send_mail_param()
    send_mail_attchment()
    print "successful"