#!/user/bin/env python
#encoding:utf-8
#__auth__=="__wanjl__"

import time
import unittest
from appium import webdriver



class addText(unittest.TestCase):

    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersionVersion']='5.1'
        desired_caps['deviceName']='wanjl'
        #desired_caps['app']=r'com.meizu.notepaper'
        desired_caps['appPackage'] = "com.meizu.notepaper"
        desired_caps['appActivity'] = "com.meizu.flyme.notepaper.app.NotePaperActivity"

        self.driver=webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_addtext(self):
        time.sleep(2)
        ele = self.driver.find_elements_by_class_name("android.widget.Button")
        ele[1].click()
        self.driver.find_element_by_accessibility_id(u'新建便签').click()
        self.driver.find_element_by_class_name('android.widget.EditText').clear()
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys('112dsfdef')
        self.driver.find_element_by_accessibility_id(u'转到上一层级').click()




if __name__=='__main__':
    suite=unittest.TestLoader().loadTestsFromTestCase(addText)
    unittest.TextTestRunner(verbosity=2).run(suite)
