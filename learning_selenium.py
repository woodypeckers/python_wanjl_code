# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestcaseLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        self.driver.get(self.base_url + "/bugfree/index.php/site/login")
        self.driver.find_element_by_id("LoginForm_username").clear()
        self.driver.find_element_by_id("LoginForm_username").send_keys("admin")
        self.driver.find_element_by_id("LoginForm_password").clear()
        self.driver.find_element_by_id("LoginForm_password").send_keys("123456")
        self.driver.find_element_by_id("SubmitLoginBTN").click()
        self.assertEqual("BugFree", self.driver.title)
        # 登录成功




    def test_case(self):
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/bug/list/1")
        driver.find_element_by_link_text(u" 新建 Bug   ").click()
        driver.switch_to.window(driver.window_handles[1])   #切换窗口
        driver.find_element_by_id("BugInfoView_title").clear() #输入之前要清空
        driver.find_element_by_id("BugInfoView_title").send_keys("bug5")
        driver.find_element_by_id("BugInfoView_assign_to_name").click()
        driver.find_element_by_css_selector("li.ac_even").click()
        driver.find_element_by_id("BugInfoView_mail_to").click()
        driver.find_element_by_xpath("//div[5]/ul/li").click()
        Select(driver.find_element_by_id("BugInfoView_severity")).select_by_visible_text("2")
        Select(driver.find_element_by_id("Custom_BugType")).select_by_visible_text(u"用户界面")
        Select(driver.find_element_by_id("Custom_HowFound")).select_by_visible_text(u"单元测试")
        driver.find_element_by_id("Custom_OpenedBuild").clear()
        driver.find_element_by_id("Custom_OpenedBuild").send_keys("123")
        driver.find_element_by_name("yt0").click()
        driver.switch_to.window(driver.window_handles[1])  # 切换窗口
        driver.close()


    def tearDown(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element_by_link_text(u"退出").click()
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
