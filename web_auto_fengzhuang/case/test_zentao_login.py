# -*- coding: utf-8 -*-
from selenium import webdriver
from case.test_login_def import ZenTao_DengLu
import time
import unittest

class LoginTest(unittest.TestCase):  # 继承unittest里的testcase框架
    '''第二个案例'''

    @classmethod
    # 只打开一次浏览器
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.zentao = ZenTao_DengLu(cls.driver)  # 调用过来先实例化

    def setUp(self):
        self.driver.get('http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html')
        self.driver.maximize_window()
        time.sleep(2)

        self.zentao.is_alert_exist()
        # 使用tearDownClass时需要清空cookies和刷新页面
        # 清空cookies 退出登陆
        self.driver.delete_all_cookies()
        # 刷新页面
        self.driver.refresh()
    def test_01(self):
        '''测试正确账号密码'''
        # 调用登陆函数
        self.zentao.login(user="admin",psw="123456")
        # 判断是否登录成功
        time.sleep(3)  # 等待页面跳转完成
        # 调用文本判断方法
        t = self.zentao.is_login_username()
        print("登陆成功，获取结果：{}".format(t))
        # 断言它为ture
        self.assertTrue(t == 'admin')

    def test_02(self):
        '''测试错误密码'''
        # 调用登陆函数
        self.zentao.login(user="admin",psw="123456789")
        # 判断是否登录成功
        time.sleep(3)  # 等待页面跳转完成
        # 获取文本 在text没有属性时如何获取到
        t = self.zentao.is_login_username()
        print("登陆失败，获取结果：{}".format(t))
        # 断言它为ture
        self.assertTrue(t == 1)  # 断言出错截图

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
