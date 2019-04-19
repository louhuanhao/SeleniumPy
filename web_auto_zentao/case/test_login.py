# -*- coding: utf-8 -*-
from selenium import webdriver
from web_auto_zentao.common.FengZhuang import WrapperFunctions
from web_auto_zentao.pages.login_page import ZenTaoLogin
import unittest
import time

url = 'http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html'


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.zl = ZenTaoLogin(cls.driver)

    def setUp(self):
        self.driver.get(url)

        # 清空cookies 退出登陆
        self.driver.delete_all_cookies()
        # 刷新页面
        self.driver.refresh()

    def test_login01(self):
        '''(user='ad', psw='123456')'''
        self.zl.login(user='ad', psw='123456')
        self.zl.isAlert()
        res = self.zl.isloginName()
        self.assertTrue(res == "")

    def test_login02(self):
        '''(user='admin', psw='123456')'''
        self.zl.login(user='admin', psw='123456')
        self.zl.isAlert()
        res = self.zl.isloginName()
        self.assertTrue(res == True)

    def test_login03(self):
        '''(user='admin', psw='1234567')'''
        self.zl.login(user='admin', psw='1234567')
        self.zl.isAlert()
        res = self.zl.isloginName()
        self.assertTrue(res == "")

    def test_login04(self):
        '''点击忘记密码'''
        self.zl.forget_login()
        self.zl.isuserReset()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
