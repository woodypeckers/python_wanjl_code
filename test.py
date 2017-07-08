#!/user/bin/env python
#encoding:utf-8

#__auth__=='__wanjl__'

import unittest
from selenium import webdriver
import time
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class TestCase1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = "http://localhost/bugfree"
        #time.sleep(2)
        self.driver.get(self.url+"/index.php/site/login")
        self.driver.find_element_by_id("LoginForm_username").clear()
        self.driver.find_element_by_id("LoginForm_username").send_keys("admin")
        self.driver.find_element_by_id("LoginForm_password").clear()
        self.driver.find_element_by_id("LoginForm_password").send_keys("123456")
        self.driver.find_element_by_id("LoginForm_rememberMe").click()
        #self.driver.find_element_by_class_name("loginbutton btn").click()
        #self.driver.find_element_by_css_selector(".loginbutton btn").click()
        self.driver.find_element_by_id("SubmitLoginBTN").click()

    # def test_bugfree_bug1_printscreen(self):
    #
    #     driver=self.driver
    #     #driver.switch_to.window(driver.window_handles[0])
    #     driver.find_element_by_link_text("自定义显示").click()
    #     driver.get_screenshot_as_file(r"D:\pythoncode\pycharm\201707080800\1.jpg")
    #
    # def test_bugfree_bug2_select(self):
    #     driver = self.driver
    #     driver.find_element_by_link_text("Case").click()
    #     Select(driver.find_element_by_id("BugFreeQuery_andor1")).select_by_visible_text(u"或者")
    #     self.driver.find_element_by_id("SaveQuery").click()
    #     self.driver.find_element_by_id("dialogQueryTitle").send_keys("test")
    #     self.driver.find_element_by_name("yt0").click()

    # def test_bugfree_bug3(self):
        #pass
        #driver=self.driver
        #driver.find_elements_by_xpath(".//*[@id='SearchConditionRow1']/td[7]/a[1]/img").click()

        #link=driver.find_elements_by_xpath(".//*[@id='SearchConditionRow1']/td[7]/a[1]/img").click()
        #ActionChains(driver).move_to_element(link).click()
        #driver.find_elements_by_xpath(".//*[@id='SearchConditionRow1']/td[7]/a[2]/img").click()

    def test_bug_free_bug4(self):

         driver=self.driver
         driver.find_element_by_partial_link_text(u"编辑我的信息").click()
         driver.find_element_by_name("yt0").click()
         driver.switch_to.window(driver.window_handles[1])
         driver.close()
         # def tearDown(self):
    #     self.driver.quit()

if __name__ == "__main__":

    #unittest.main()
    suits=unittest.TestSuite()
    loader=unittest.TestLoader()
    suits.addTests(loader.loadTestsFromTestCase(TestCase1))
    #fp = open(r'D:\pythoncode\pycharm\201707080800\test_result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    #runner = HTMLTestRunner(stream=fp,
                            #title=u'bugfree测试报告',
                            #description=u"测试用例执行情况：")
    #runner.run(suits)
    unittest.TextTestRunner(verbosity=2).run(suits)







