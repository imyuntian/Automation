import requests
import unittest
import json


class LoginByPasswordTest(unittest.TestCase):
    ''' 测试PC端【通过密码登录】接口：login_by_password '''

    def setUp(self):
        self.url = 'https://testcns.xiudream.com/api/user/login/login_by_password'
        self.headers = {'Content-Type': 'application/raw'}

    def tearDown(self):
        print("响应数据：%s" % self.result)

    def test_login0(self):
        ''' 登录成功 '''

        self.req = {"password": "1234qwer", "username": "18612136611", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')
        self.assertEqual(self.result['data']['user_info']['aliasName'], '18612136611')

    def test_login1(self):
        ''' 账号正确，密码错误 '''

        self.req = {"password": "errorpwd1", "username": "18384156109", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '10007')
        self.assertEqual(self.result['msg'], '用户名或密码错误，你还有9机会')

    def test_login2(self):
        ''' 账号错误，密码正确 '''

        self.req = {"password": "1234qwer", "username": "username2", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '10006')
        self.assertEqual(self.result['msg'], '该帐号无权限登录CNS')

    def test_login3(self):
        ''' 账号为空 '''

        self.req = {"password": "1234qwer", "username": "", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '1')
        self.assertEqual(self.result['msg'], '参数 username 不能为空')

    def test_login4(self):
        ''' 密码为空 '''

        self.req = {"password": "", "username": "15198139787", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '1')
        self.assertEqual(self.result['msg'], '参数 password 不能为空')

    def test_login5(self):
        ''' 账号是一个空格 '''

        self.req = {"password": "1234qwer", "username": " ", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '1')
        self.assertEqual(self.result['msg'], '参数 username 不能为空')

    def test_login6(self):
        ''' 密码是一个空格 '''

        self.req = {"password": " ", "username": "18328578126", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '1')
        self.assertEqual(self.result['msg'], '参数 password 不能为空')

    def test_login7(self):
        ''' 账号是html标签 '''

        self.req = {"password": "1234qwer", "username": "<script></script>", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '10006')
        self.assertEqual(self.result['msg'], '该帐号无权限登录CNS')

    def test_login8(self):
        ''' 账号是html标签 '''

        self.req = {"password": "<script></script>", "username": "15657169205", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '10007')
        self.assertEqual(self.result['msg'], '用户名或密码错误，你还有9机会')

    def test_login9(self):
        ''' 账号是JS函数 '''

        self.req = {"password": "1234qwer", "username": "<script>alert(\"hello\")</script>", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '10006')
        self.assertEqual(self.result['msg'], '该帐号无权限登录CNS')

    def test_login10(self):
        ''' 密码是JS函数 '''

        self.req = {"password": "<script>alert(\"hello\")</script>", "username": "15025316959", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '10007')
        self.assertEqual(self.result['msg'], '用户名或密码错误，你还有9机会')

    def test_login11(self):
        ''' 密码正确时，账号是超11位手机号 '''

        self.req = {"password": "1234qwer", "username": "133211554330", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        # self.assertEqual(self.result['code'], 'xxxxx')
        self.assertEqual(self.result['msg'], '请输入正确的手机号')

    def test_login12(self):
        ''' 正确账号开头有空格 '''

        self.req = {"password": "1234qwer", "username": " 13321155433", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')
        
    def test_login13(self):
        ''' 正确账号中间有空格 '''

        self.req = {"password": "1234qwer", "username": "133211 55433", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')

    def test_login14(self):
        ''' 正确账号末尾有空格 '''

        self.req = {"password": "1234qwer", "username": "13321155433 ", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')

    def test_login15(self):
        ''' 简单SQL注入：账号任意，密码输入 'OR'1'='1 '''

        self.req = {"password": "'OR'1'='1", "username": "13321155433 ", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')


if __name__ == '__main__':
    # unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    tests = []
    i = 0
    while i <= 15:  # 跟最后一个测试案例的数字一致，增加案例时，这里要改
        tests.append(LoginByPasswordTest("test_login%d" %i))
        i += 1

    print(tests)
    suite.addTests(tests)

    runner = unittest.TextTestRunner()
    runner.run(suite)