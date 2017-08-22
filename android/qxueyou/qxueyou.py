#!/user/bin/env python
#encoding:utf-8
#__auth__=="__wanjl__"

from appium import  webdriver
import unittest,time


class Qxueyou(unittest.TestCase):

    def setUp(self):

        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion'] ='5.1'
        desired_caps['deviceName']='71MBBL323CPL'
        #Q学友的app
        desired_caps['app']=r'C:\Users\Administrator\Desktop\com.iqtogether.qxueyou_233.apk'

        self.driver=webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


    def tearDown(self):

        self.driver.quit()


    def test_login(self):

        driver=self.driver
        els=driver.find_elements_by_class_name("android.widget.Button")
        els[2].click()
        time.sleep(2)
        #driver.find_element_by_accessibility_id(u'注册').click()
        els2=driver.find_elements_by_class_name('android.widget.EditText')
        els2[0].clear()
        els2[0].send_keys('18576672691')
        driver.find_element_by_class_name("android.widget.Button").click()
        els2[1].clear()
        els2[1].send_keys("123456")
        #self.assert_equle(u"错误",)

if __name__ == '__main__':

    suite=unittest.TestLoader().loadTestsFromTestCase(Qxueyou)
    unittest.TextTestRunner(verbosity=2).run(suite)
