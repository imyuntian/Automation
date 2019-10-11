
from appium import webdriver

capabilities = {}

capabilities['platformName'] = 'Android'
capabilities['platformVersion'] = '5.1'
capabilities['deviceName'] = 'huawei'

capabilities['appPackage'] = 'com.android.settings'
capabilities['appActivity'] = '.Settings'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)

