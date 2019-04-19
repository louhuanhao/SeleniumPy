# -*- coding: utf-8 -*-
from selenium import webdriver
from web_auto_zentao.common.FengZhuang import WrapperFunctions
import time

url = "http://127.0.0.1:82/zentao/user-login-L3plbnRhby8=.html"


class ZenTaoLogin(WrapperFunctions):  # 继承
    # 定位登陆
    loc1 = ("id", "account")
    loc2 = ("xpath", '//*[@id="login-form"]/form/table/tbody/tr[2]/td/input')
    loc3 = ("xpath", '//*[@id="submit"]')
    loc_keep_login = ("id", "keepLoginon")
    loc_for_psw = ("link text", "忘记密码")
    loc_user_reset = ('link text', '刷新')
    loc_username = ('xpath', '//*[@id="userMenu"]/a')

    def inputUser(self, ur=''):
        self.sendKeys(self.loc1, ur)

    def inputPsw(self, pw=""):
        self.sendKeys(self.loc2, pw)

    def clickbutton01(self):
        self.click(self.loc3)

    def keeplogin(self, keep_login=False):
        '''保持登陆开关'''
        if keep_login:
            self.click(self.loc_keep_login)

    def forget_login(self):
        '''忘记密码'''
        self.click(self.loc_for_psw)

    def isAlert(self):
        '''判断alert窗口 '''
        a = self.isAlertExist()
        if a:
            print(a)
        else:
            print("无弹窗")

    def isuserReset(self):
        '''判断点击忘记密码跳转成功'''

        a = self.isTextInElement(self.loc_user_reset, '刷新')
        if a:
            print("跳转成功")
        else:
            print("跳转失败")


    def isloginName(self):
        '''判断是否登陆成功，获取登陆名'''
        name = self.isGetText(self.loc_username)
        return name

    def login(self, user='admin', psw='123456', keep_login=False):
        '''登陆'''
        self.driver.get(url)
        self.inputUser(user)
        self.inputPsw(psw)
        self.clickbutton01()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    ztl = ZenTaoLogin(driver)
    ztl.driver.get(url)
    ztl.forget_login()
    ztl.isuserReset()
