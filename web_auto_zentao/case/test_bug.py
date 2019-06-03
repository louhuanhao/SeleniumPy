# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from web_auto_zentao.pages.add_Bug_page import ZenTaoBug
from web_auto_zentao.pages.login_page import ZenTaoLogin


class test_AddBug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

        cls.ztb = ZenTaoBug(cls.driver)
        ztl = ZenTaoLogin(cls.driver)
        ztl.login()

    def test_add_Bug(self):
        strsj = time.strftime("%Y_%m_%d_%H_%M_%S")
        tit = '@id=_openedBuild_chosen_]_div_ul_li' + strsj
        self.ztb.addBug(tit)
        res = self.ztb.asnewBug(tit)
        if self.assertTrue(res):
            print('添加成功')
        else:
            print('添加失败')


if __name__ == "__main__":
    unittest.main()
