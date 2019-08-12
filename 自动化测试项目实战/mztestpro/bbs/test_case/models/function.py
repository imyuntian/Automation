from selenium import webdriver
import os


# 截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # 注意os用法
    base_dir = str(base_dir)  # 二进制流转成字符串
    base_dir = base_dir.replace('\\', '/')  # 程序里用左斜杠，所以此处替换处理一下
    base = base_dir.split('/test_case')[0]  # 以/test_case进行分割，取第一个元素
    file_path = base + '/report/image' + file_name
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    insert_img(driver, "baidu.jpg")
    driver.quit()
