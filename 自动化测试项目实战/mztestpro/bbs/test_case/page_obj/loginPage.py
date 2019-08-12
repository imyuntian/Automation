from selenium.webdriver.common.action_chains import ActionChains  # 操作鼠标
from selenium.webdriver.common.by import By  # 用By定位元素 By来声明定位的方法，并且传入对应定位方法的定位参数
from .base import Page
from time import sleep


class login(Page):
    """
    用户登录页面
    创建登录页面对象，对用户登录页上的用户名/密码输入框、登录按钮和提示信息等元素的定位进行封装
    创建user_login()作为系统统一登录的入口
    对操作步骤的封装既可以放在Page Object当中，也可以放在测试用例中，具体情况具体分析
    这里放在Page Object中，是考虑到还有其他用例会调用该登录方法
    """

    url = '/'

    # Action
    '''bbs社区获取登录用户名的定位方法的参数'''
    bbs_login_user_loc = (By.XPATH, "//div[@id='mzCust']/div/img")  # 这个运行时可能会改
    '''bbs社区获取登录按钮的定位方法的参数'''
    bbs_login_button_loc = (By.ID, "mzLogin")  # 小括号，代表tuple元组数据类型，不可变序列

    def bbs_login(self):
        self.find_element(
            *self.bbs_login_user_loc).click()  # 相当于 find_element(By.XPATH, "//div[@id='mzCust']/div/img")   By定位元素
        sleep(1)
        self.find_element(*self.bbs_login_button_loc).click()

    '''获取账户名、密码框、登录按钮的定位方法的参数'''
    login_username_loc = (By.ID, "account")
    login_password_loc = (By.ID, "password")
    login_button_loc = (By.ID, "login")

    # 定位上面的元素：登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    # 定位上面的元素：登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    # 定位上面的元素：登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一登录入口
    def user_login(self, username="username", password='1111'):
        """
        获取的用户名密码登录
        登录方法，调用这个就登录呗
        """
        self.open()
        self.bbs_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    user_error_hint_loc = (By.XPATH, "//span[@for='account']")
    pawd_error_hint_log = (By.XPATH, "//span[@for='password']")
    user_login_success_loc = (By.ID, "mzCustName")

    # 用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    # 密码错误提示
    def pawd_error_hint(self):
        return self.find_element(*self.pawd_error_hint_log).text

    # 登录成功用户名
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text
