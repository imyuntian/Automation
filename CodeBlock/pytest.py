#=== 打开测试机系统设置 ===#

from appium import webdriver

# 初始化参数数组
capabilities = {}
# 安卓测试平台
capabilities['platformName'] = 'Android'
# 系统版本
capabilities['platformVersion'] = '5.1'
# 设备名称
capabilities['deviceName'] = 'huawei'
# APP包名
capabilities['appPackage'] = 'com.android.settings'
capabilities['appActivity'] = '.Settings'
# 连接测试机所在服务器
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)

