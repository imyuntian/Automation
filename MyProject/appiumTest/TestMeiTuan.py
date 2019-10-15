"""
使用夜神模拟器，在美团APP里，进行了简单的自动化测试练习
"""
"""
踩坑如下：
1、使用xpath时，后面的class写错了；(如果实在不知道class，就写*)
2、字典的用法记得不牢
2.1 这更像是JAVA写法
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
2.2 PYTHON写法
    desired_caps = {'platformName': 'Android'}
3、for语法忘记
4、定义数组的写法写成了Java写法
"""
# from time import *
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '5.1',
    'deviceName': 'HUAWEI',
    'appPackage': 'com.sankuai.meituan',
    'appActivity': '.activity.MainActivity',
    'noReset': True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


def test_top_btn():
    # 循环点击这些导航按钮
    args = ['美食', '电影', '酒店', 'KTV', '今日新单', '周边游', '西餐']
    for arg in args:
        # print(arg)
        # driver.find_element_by_xpath("//android.widget.TextView[@text='美食']").click()
        driver.find_element_by_xpath("//android.widget.TextView[@text='" + arg + "']").click()
        sleep(2)
        driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='android:id/home']").click()
        # 如果不知道元素的class属性，可以用 * 代替
        # driver.find_element_by_xpath("//*[@resource-id='android:id/home']").click()
        sleep(2)


def click_list():
    elements = driver.find_elements_by_id("com.sankuai.meituan:id/title")
    for elemt in elements:
        elemt.click()
        sleep(1)
        driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='android:id/home']").click()
        sleep(1)


# 自动点击首页团购列表（点一屏之后再滑动一屏，再点一屏）
def test_list():
    click_list()
    driver.swipe(start_x=646,start_y=1442,end_x=646,end_y=450)
    sleep(2)
    click_list()




# 当ID属性不唯一的时候，可以使用elements
def find_by_ids():
    elements = driver.find_elements_by_id('com.sankuai.meituan:id/title')
    elements[2].click()


if __name__ == '__main__':
    # test_top_btn()
    # find_by_ids()
    test_list()

