"""
使用夜神模拟器，在美团APP里，进行了简单的自动化测试练习
"""
import time
from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1',
    'deviceName': 'HUAWEI',
    'appPackage': 'com.sankuai.meituan',
    'appActivity': '.activity.MainActivity',
    'noReset': True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 循环点击这些导航按钮
args = ['美食', '电影', '酒店', 'KTV', '今日新单', '周边游', '西餐']
for arg in args:
    # print(arg)
    # driver.find_element_by_xpath("//android.widget.TextView[@text='美食']").click()
    driver.find_element_by_xpath("//android.widget.TextView[@text='" + arg + "']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='android:id/home']").click()
    # 如果不知道元素的class属性，可以用 * 代替
    # driver.find_element_by_xpath("//*[@resource-id='android:id/home']").click()
    time.sleep(2)

"""
踩坑如下：
1、使用xpath时，后面的class写错了；(如果实在不知道class，就写*)
2、字典的用法记得不牢
3、for语法忘记
4、定义数组的写法写成了Java写法
"""


