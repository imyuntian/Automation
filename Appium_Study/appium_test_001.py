from appium import webdriver

# 启动参数
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'huawei'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

# 声明手机驱动对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)