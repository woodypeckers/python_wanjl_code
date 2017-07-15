#!/user/bin/env python
#encoding:utf-8
#__auth__=="__wanjl__"

from unittest import TestCase
from selenium import webdriver

class TestLogin(TestCase):

    def test_bugfree_login(self):
       self.driver=webdriver.Chrome(executable_path=r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe')
       self.driver.get("http://localhost/bugfree/")
       self.driver.find_element_by_id("LoginForm_username").clear()
       self.driver.find_element_by_id("LoginForm_username").send_keys("admin")
       self.driver.find_element_by_id("LoginForm_password").clear()
       self.driver.find_element_by_id("LoginForm_password").send_keys("123456")
       self.driver.find_element_by_id("LoginForm_rememberMe").click()
       self.driver.find_element_by_id("SubmitLoginBTN").click()

