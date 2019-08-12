# coding=utf-8
from selenium.webdriver import Remote
from selenium import webdriver


# 启动浏览器驱动
def browser():
    # driver = webdriver.Chrome()
    print("1")
    host = '127.0.0.1:4444'          # 运行主机：端口号（本机默认：127.0.0.1:4444）
    dc = {'browserName': 'chrome'}   # 指定浏览器
    strhost = 'http://' + host + '/wd/hub'
    print("%s" %strhost)
    print("1.1")
    driver = Remote(command_executor=strhost, desired_capabilities=dc)
    print("2")
    return driver


if __name__ == '__main__':
    dr = browser()
    print("3")
    dr.get("http://www.baidu.com")
    print(dr.title)
    print("4")
    dr.quit()
