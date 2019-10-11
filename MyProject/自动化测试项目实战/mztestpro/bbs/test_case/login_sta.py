# 假设登录页的对象命名为loginPage.py，那么关于测试登录的用例文件应该命名为login_sta.py
# 这样方便用例报错时问题的追踪。尽量把一个页面上的元素定位封装到一个 "*Page.py"文件中，把针对这个页面的测试用例集中到一个"*_sta.py"
from time import sleep
import unittest, random, sys

sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit, function
from page_obj.loginPage import login


class loginTest(myunit.MyTest):  # loginTest继承MyTest 省去了在每个测试类中实现一遍setUp()和tearDown()
    """社区登录测试"""

    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        login(self.driver).user_login(username, password)  # login(self.driver) 实例化login类

    def test_login1(self):
        """用户名、密码为空登录"""
        self.user_login_verify()  # 用户名密码都为空; 方法调用之前,先执行了setUp(),所以login(self.driver)是没问题的，实例化login类的时候，传入self.driver
        po = login(self.driver)  # 点击登录
        self.assertEqual(po.user_error_hint(), "账号不能为空")  # 断言，看有没有报错
        self.assertEqual(po.pawd_error_hint(), "密码不能为空")  # 断言，看有没有报错
        function.insert_img(self.driver, "user_pawd_empty.jpg")  # 截图保存

    def test_login2(self):
        """用户名正确，密码为空登录"""
        self.user_login_verify(username="pytest")  # 因为这里的verify函数的参数有默认值，所以此处的password不传参数，既为空
        po = login(self.driver)
        self.assertEqual(po.pawd_error_hint(), "密码不能为空")
        function.insert_img(self.driver, "pawd_empty.jpg")

    def test_login3(self):
        """用户名为空，密码正确"""
        self.user_login_verify(password="abc123456")
        po = login(self.driver)
        self.assertEqual(po.user_error_hint(), "账号不能为空")
        function.insert_img(self.driver, "user_empty.jpg")

    def test_login4(self):
        """用户名与密码不匹配"""
        character = random.choice('zyxwvutsrqponmlkjihgfedcba')
        username = "zhangsan" + character  # 用户名随机变化，避免“反复使用错误的用户名和密码，系统会弹出验证码”
        self.user_login_verify(username=username, password="123456")
        po = login(self.driver)
        self.assertEqual(po.pawd_error_hint(), "密码与账号不匹配")
        function.insert_img(self.driver, "user_pawd_error.jpg")

    def test_login5(self):
        """用户名、密码正确"""
        self.user_login_verify(username="zhangsan", password="123456")
        sleep(2)
        po = login(self.driver)
        self.assertEqual(po.user_login_success(), '张三')  # 获取用户名作为断言信息。用户名是张三，说明登录成功
        function.insert_img(self.driver, "user_pawd_ture.jpg")


if __name__ == "__main__":
    unittest.main()
