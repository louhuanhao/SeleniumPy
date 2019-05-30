# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import unittest


class ZenTao_DengLu():
    def __init__(self, driver):
        self.driver = driver

    def login(self, user, psw):
        self.driver.find_element_by_xpath('//*[@id="account"]').send_keys(user)
        self.driver.find_element_by_xpath('//*[@id="login-form"]/form/table/tbody/tr[2]/td/input').send_keys(psw)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

    def is_login_username(self):
        '''判断文本方法，有则输出text，没有输出空'''
        try:
            time.sleep(3)
            t = self.driver.find_element_by_xpath('//*[@id="userMenu"]/a').text
            print(t)
            return t
        except:
            return ""

    def is_alert_exist(self):
        '''判断是否有alert，有则关闭，没有pass'''
        try:
            # 获取alert
            al = self.driver.switch_to.alert
            # 获取alert值
            text = al.text
            # 关闭alert弹窗
            al.accept()
            return text
        except:
            return ""


if __name__ == "__main__":
    driver = webdriver.Firefox()
    ZenTao_DengLu.login(driver)
