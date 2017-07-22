#!/user/bin/env python
#encoding:utf-8

import  os,threading
import Queue,xlrd,time
from selenium import webdriver

def test_quene():
    current_dir=os.getcwd()
    print current_dir
    data=xlrd.open_workbook(r"%s/login.xlsx" %current_dir)
    table=data.sheets()[0]
    print table.nrows
    for i in range(table.nrows):
        if i==0:
            continue
        dict=table.row_values(i)
        print dict
    return  dict

def  test_2(self):

    print "this is another thread"

def main():
    threads=[]

    t1=threading.Thread(target=test_quene)
    threads.append(t1)

    t2 = threading.Thread(target=test_2)
    threads.append(t2)

    for i in threads:
        i.start()

    for i in threads:
        i.join()

    print "all done"







if __name__=="__main__":
    main()

    dict=test_quene()
    print dict
    data=Queue.Queue()
    data.put(dict)
    for i in range(3):

        print data.get()[i]
    # print data.get()[0]
    # print data.get()[1]

    try:
        data.empty()
    except:
        print "the quene is empty"



    url="http://localhost/bugfree/index.php/bug/list/1"
    driver=webdriver.Chrome(executable_path="C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    driver.get(url)
    driver.find_element_by_id("LoginForm_username").clear()
    driver.find_element_by_id("LoginForm_username").send_keys(data.get()[0])
    driver.find_element_by_id("LoginForm_password").clear()
    driver.find_element_by_id("LoginForm_password").send_keys(data.get()[1])
    driver.find_element_by_id("SubmitLoginBTN").click()
    time.sleep(3)
    driver.close()








