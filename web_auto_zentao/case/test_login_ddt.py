# -*- coding: utf-8 -*-
from selenium import webdriver
from web_auto_zentao.common.FengZhuang import WrapperFunctions
from web_auto_zentao.pages.login_page import ZenTaoLogin
from web_auto_zentao.common.read_xlsx import ExcelUtil
import unittest
import ddt
import os
import time

url = 'http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html'
# 读取xlsx数据
propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
p = os.path.join(propath, "common", "zentao.xlsx")
# p = "D:\\BaiduNetdiskDownload\\zentao.xlsx"
n = "Sheet1"
data = ExcelUtil(p, n)
testdates = data.dict_data()


@ddt.ddt
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

    def login_ddt(self, user, psw, expect):
        '''user账号 psw密码 expect期望值'''
        self.zl.login(user, psw)
        self.zl.isAlert()
        res = self.zl.isloginName()
        print("返回结果:{}".format(res))
        self.assertTrue(res == expect)

    @ddt.data(*testdates)
    def test_login(self, data):
        '''ddt驱动传入'''
        print("------------开始测试------------")
        self.login_ddt(data["user"], data["psw"], data["expect"])
        print("------------结束测试------------")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
