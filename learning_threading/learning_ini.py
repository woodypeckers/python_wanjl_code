#!/user/bin/env python
#encoding:utf-8
#__auth__=="__wanjl__"

import ConfigParser
import os

def iniconfig_write_read():

    config=ConfigParser.ConfigParser()    #模块中的类
    current_dir=os.getcwd()
    print current_dir
    try:
        os.path.exists("%s/systerm.ini" %current_dir)
    except:
        config.read("%s/systerm.ini" %current_dir)
    config.add_section("abp_sh")
    config.set("abp_sh","ip","192.168.161.1")
    config.set("abp_sh","user","abp_sh")
    config.set("abp_sh","password","abp_sh")
    config.add_section("abp_sx")
    config.set("abp_sx","user","abp_sx")
    config.set("abp_sx","password","abp_sx")
    config.write(open("systerm.ini","w"))
    print config.get("abp_sh","ip")
    print config.read("systerm.ini")    #输出字符串为：systerm.ini
    print  config.has_option("abp_ah","ip")
    print  config.items("abp_sh")
    config.remove_section("abp_sh")
    try:
        config.getboolean("abp_sh","user")
    except:
        print  "this dsn doesn't exist"






if __name__=="__main__":
    print "hello"
    iniconfig_write_read()



