# 用例执行程序
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.text import MIMEText
import smtplib
import unittest
import time
import os


# ==========定义发送邮件==========
def send_mail(file_new):
    f = open(file_new, 'rb')  # ./bbs/report\2019-08-14 01_25_35result.html
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From'] = 'hslworkz6<hslworkz6@126.com>'
    msg['To'] = 'hslworkz6<hslworkz6@126.com>'

    smtp = smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("hslworkz6@126.com", "admin123")  # 授权码admin123
    smtp.sendmail("hslworkz6@126.com", "hslworkz6@126.com", msg.as_string())  # 3个参数：发、收、内容
    smtp.quit()
    print('email has send out !')


# ==========查找测试报告目录，找到最新生成的测试报告文件==========
def new_report(testreport):
    lists = os.listdir(testreport)  # 返回指定的文件夹包含的文件或文件夹的名字的列表
    # print(lists)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))  # 用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。  lambda表达式
    # print(lists)
    # print(lists[-1])
    file_new = os.path.join(testreport, lists[-1])  # 将多个路径组合后返回     lists[-1] 排序后的最后一个元素
    # print(file_new)
    return file_new  # ./bbs/report\2019-08-14 01_18_42result.html


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './bbs/report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='魅族社区自动化测试报告', description='环境：windows 10 浏览器：chrome')
    discover = unittest.defaultTestLoader.discover('./bbs/test_case', pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    file_path = new_report('./bbs/report')  # 查找新生成的报告
    send_mail(file_path)  # 调用发邮件模块
