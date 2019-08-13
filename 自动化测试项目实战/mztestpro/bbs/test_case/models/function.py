from selenium import webdriver
import os


# 截图函数
def insert_img(driver, file_name):
    # print(os.path.dirname(__file__)) # D:/LocalAutomation/test03/Automation/自动化测试项目实战/mztestpro/bbs/test_case/models  os.path.dirname(__file__):获取当前文件所在目录
    base_dir = os.path.dirname(os.path.dirname(__file__))  # 注意os用法  获取models目录所在的目录，即test_case
    # print(base_dir) # D:/LocalAutomation/test03/Automation/自动化测试项目实战/mztestpro/bbs/test_case
    base_dir = str(base_dir)  # 二进制流转成字符串
    base_dir = base_dir.replace('\\', '/')  # 程序里用左斜杠，所以此处替换处理一下      但是经过打印查看，替换前后并无差别。
    # print(base_dir)
    base = base_dir.split('/test_case')[0]  # 以/test_case进行分割，取第一个元素，即：D:/LocalAutomation/test03/Automation/自动化测试项目实战/mztestpro/bbs
    file_path = base + '/report/image/' + file_name
    # print(file_path)
    driver.get_screenshot_as_file(file_path)


"""测试截图函数是否好用"""
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    insert_img(driver, "baidu.png")
    driver.quit()
