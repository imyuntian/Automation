#######################################
#  点击联系人APP界面中[添加联系人]按钮  #
#######################################
import time
from appium import webdriver

# 参数数组初始化
capabilities = {}
# 安卓平台测试
capabilities['platformName'] = 'Android'
# 测试设备版本
capabilities['platformVersion'] = '5.1'
# 设备名，随便起
capabilities['deviceName'] = 'Android Emulator'
# 联系人APP的包名
capabilities['appPackage'] = 'com.android.contacts'
# 联系人APP的主入口
capabilities['appActivity'] = '.activities.PeopleActivity'
#
capabilities['unicodeKeyboard'] = True
capabilities['resetKeyboard'] = True
# 连接测试机所在服务器
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)

try:
    # 通过系统框架进行异常截图
    element = driver.find_element_by_id('com.android.contacts:id/floating_action_button')
    # 如果找到该ID所指定控件，则进行点击操作
    element.click()
except:
    print('exist')
    pass

time.sleep(2)
# 断开连接
driver.quit()