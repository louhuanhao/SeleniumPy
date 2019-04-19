# -*- coding: utf-8 -*-
from selenium import webdriver
from web_auto_zentao.common.FengZhuang import WrapperFunctions
from web_auto_zentao.pages.login_page import ZenTaoLogin
import time


class ZenTaoBug(WrapperFunctions):  # 继承

    # 定位bug
    loc4 = ("link text", "测试")
    loc5 = ("link text", "Bug")
    loc6 = ("xpath", '//*[@id="createActionMenu"]/a')
    loc_truck1 = ("xpath", '//*[@id="openedBuild_chosen"]/ul')
    loc_truck2 = ("xpath", '//*[@id="openedBuild_chosen"]/div/ul/li')
    loc_title = ("id", 'title')
    loc_boby = ("class name", "article-content")  # 需要先切换表单
    loc_baocun = ("css selector", "#submit")
    loc_newbug = ("xpath", '//*[@id="bugList"]/tbody/tr/td[4]/a')

    def addBug(self, bugtitle):
        '''添加bug'''
        self.click(self.loc4)
        self.click(self.loc5)
        self.click(self.loc6)
        self.click(self.loc_truck1)
        self.click(self.loc_truck2)
        # 输入标题
        self.sendKeys(self.loc_title, bugtitle)
        # 切换iframe
        self.driver.switch_to.frame(0)
        # 输入正文
        self.sendKeys(self.loc_boby, "好胜人 耻闻过 骋辩给 炫聪明 厉威严 姿强愎 ")
        # 跳出iframe
        self.driver.switch_to.default_content()
        self.click(self.loc_baocun)

    def asnewBug(self, bugtitle):
        '''查看新bug标题是否与预期一致'''
        return self.isTextInElement(self.loc_newbug, bugtitle)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    ztb = ZenTaoBug(driver)
    ztl = ZenTaoLogin(driver)
    ztl.login()
    strsj = time.strftime("%Y_%m_%d_%H_%M_%S")
    tit = '@id=_openedBuild_chosen_]_div_ul_li' + strsj
    ztb.addBug(tit)
    res = ztb.asnewBug(tit)
    print(res)
    driver.assertTrue(res)
