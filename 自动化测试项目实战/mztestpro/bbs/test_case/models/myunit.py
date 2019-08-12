# 自定义测试框架类
from selenium import webdriver
from .driver import browser  # .driver 为何用.?  为何导browser而不是直接用webdriver?  因为这里导入的不是系统的，调用的是当前目录下driver.py里的browser函数
import unittest
import os


# 把setUp()和tearDown() 抽象出来，编写测试用例时，不再考虑这两个方法的实现
class MyTest(unittest.TestCase):
    """
    setUp/tearDown：在测试用例的开始于结束时被执行
    """

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)  # 隐式等待10秒
        self.driver.maximize_window()  # 浏览器全屏显示

    def tearDown(self):
        self.driver.quit()
