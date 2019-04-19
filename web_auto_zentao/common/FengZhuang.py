# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 显式等待
from selenium.common.exceptions import *  # 导入所有的异常
from selenium.webdriver.support import expected_conditions as EC  # 用EC代替expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.support.select import Select
import time


# driver = webdriver.Chrome()
# driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
# driver.maximize_window()
# time.sleep(2)


# # 封装定位方法
# def findElement(driver, loc, time=5, fre=0.5):
#     '''封装方法'''
#     ele = WebDriverWait(driver, time, fre).until(lambda x: x.find_element(*loc))#*loc 依次传入
#     return ele
# loc1=(By.ID,"account")
# loc2=(By.NAME,"password")
# loc3=(By.ID,"submit")
#
# findElement(driver,loc1).send_keys("admin")
# findElement(driver,loc2).send_keys("123456")
# findElement(driver,loc3).click()


# 封装定位函数
class WrapperFunctions():
    '''封装函数'''

    # 定义一个公共类,driver:让形参对应上这个类，在继承时才能调用driver
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.time = 5
        self.fre = 0.5

        # 单个元素定位不到会抛NoSuchElementException异常，但是复数定位不到就要返回空list，不抛异常

    def findElementEC(self, loc):
        '''定位到元素，返回元素对象。没有定位到，返回Timeout异常'''
        if not isinstance(loc, tuple):
            print("loc参数类型错误，必须传元组")
        else:
            print("正在定位元素信息:定位方式→{}, VALUE值→{}".format(loc[0], loc[1]))
            ele = WebDriverWait(self.driver, self.time, self.fre).until(EC.presence_of_element_located(loc))
            return ele

    def findElement(self, loc):  # loc=(By_ID,"nr")
        # 显示等待找到这个元素并返回
        '''定位单个元素返回'''
        if not isinstance(loc, tuple):
            print("loc参数类型错误，必须传元组")
        else:
            print("正在定位元素信息:定位方式→{}, VALUE值→{}".format(loc[0], loc[1]))
            ele = WebDriverWait(self.driver, self.time, self.fre).until(lambda x: x.find_element(*loc))  # *loc 依次传入
            return ele

    def findElements(self, loc):  # loc=(By_ID,"nr")
        # 显示等待找到这个元素并返回
        '''定位复元素返回'''
        try:
            ele = WebDriverWait(self.driver, self.time, self.fre).until(lambda x: x.find_elements(*loc))  # *loc 依次传入
            return ele
        except:
            return []

    def isElementExist(self, loc):
        '''判断单个元素有没有被找到'''
        try:
            self.findElement(loc)
            return True
        except:
            return False

    def isElementExists(self, loc):
        '''判断复选元素有没有被找到'''
        eles = self.findElements(loc)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            print("定位到一个元素")
            return True
        else:
            print("定位到元素的个数为:", n)
            return True

    def sendKeys(self, loc, text):
        '''输入数据'''
        ele = self.findElement(loc)
        ele.send_keys(text)

    def click(self, loc):
        '''点击操作'''
        ele = self.findElement(loc)
        ele.click()

    def isSelected(self, loc):
        '''判断selected是否被选中'''
        ele = self.findElement(loc).is_selected()
        return ele

    def isDisplayed(self, loc):
        '''判断元素在dom里显示，隐藏，不存在报TimeoutException异常'''
        ele = self.findElement(loc).is_displayed()
        return ele

    def isEnabled(self, loc):
        '''判断元素可以被操作'''
        ele = self.findElement(loc).is_enabled()
        return ele

    def isTitle(self, title):
        '''判断当前title是否等于预期的string，返回布尔值'''
        try:
            res = WebDriverWait(self.driver, self.time, self.fre).until(EC.title_is(title))
            return res
        except:  # 如果超时就返回False
            return False

    def isTitleContains(self, title):
        '''判断当前title是否包含预期的string，返回布尔值'''
        try:
            res = WebDriverWait(self.driver, self.time, self.fre).until(EC.title_contains(title))
            return res
        except:
            return False

    def isTextInElement(self, loc, text):
        '''判断某个元素的中的text是否包含了预期的string，返回布尔值'''
        try:
            res = WebDriverWait(self.driver, self.time, self.fre).until(EC.text_to_be_present_in_element(loc, text))
            return res
        except:
            return False

    def moveToElement(self, loc):
        '''鼠标悬停'''
        ele = self.findElement(loc)
        ActionChains(driver).move_to_element(ele).perform()

    def selectByIndex(self, loc, idx=0):
        '''通过索引定位select，index从0开始，默认第一个'''
        ele = self.findElement(loc)
        Select(ele).select_by_index(idx)

    def selectByValue(self, loc, val):
        '''通过value属性定位select'''
        ele = self.findElement(loc)
        Select(ele).select_by_value(val)

    def selectByText(self, loc, text):
        '''通过文本值定位select'''
        ele = self.findElement(loc)
        Select(ele).select_by_visible_text(text)

    def jsScrollEnd(self):
        '''滚动到底部'''
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)

    def jsScrollfist(self):
        '''滚动到顶部'''
        js = "var q=document.getElementById('id').scrollTop=0"
        self.driver.execute_script(js)

    def jsScroll(self, loc):
        '''聚焦元素'''
        ele = self.findElement(loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    def isAlertExist(self):
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

    def isGetText(self, loc):
        '''获取属性的TEXT值'''
        try:
            tx = self.findElement(loc).text
            return tx
        except:
            return ''


# 测试
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
    driver.maximize_window()
    time.sleep(2)
    zentao = WrapperFunctions(driver)  # 调用这个类，返回实例
    loc1 = (By.ID, "account")  # 不导入By包时，对应("id","account")
    loc2 = (By.NAME, "password")  # 对应("name","password")
    loc3 = (By.ID, "submit")

    zentao.sendKeys(loc1, "admin")
    zentao.sendKeys(loc2, "123456")
    zentao.click(loc3)
