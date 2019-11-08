import requests
import unittest
import json


class LoginBySMSCodeTest(unittest.TestCase):
    ''' 测试PC端【通过短信验证码登录】接口：login_by_sms_code '''

    def setUp(self):
        self.url = 'https://testcns.xiudream.com/api/user/login/login_by_sms_code'
        self.headers = {'Content-Type': 'application/raw'}
        self.smscode = "765854"  # 执行前，先用手机获取验证码，手动改一下这个配置

    def tearDown(self):
        print("响应数据：%s" % self.result)

    def test_login0(self):
        ''' 验证码错误 '''

        self.req = {"mobile": "13321155433", "code": self.smscode, "login_type": 1}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '3')
        self.assertEqual(self.result['msg'], '短信验证码错误')
        # self.assertEqual(self.result['data']['user_info']['aliasName'], '18612136611')

    def test_login1(self):
        ''' 验证码为空 '''

        self.req = {"mobile": "13321155433", "code": "", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '1')
        self.assertEqual(self.result['msg'], '验证码不能为空')

    def test_login2(self):
        ''' 验证码含有汉字 '''

        self.req = {"mobile": "13321155433", "code": "验证码汉字", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '3')
        self.assertEqual(self.result['msg'], '短信验证码错误')

    def test_login3(self):
        ''' 验证码含有6个空格 '''

        self.req = {"mobile": "13321155433", "code": "      ", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '3')
        self.assertEqual(self.result['msg'], '短信验证码错误')

    def test_login4(self):
        ''' 验证码超过6位 '''

        self.req = {"mobile": "13321155433", "code": "1234567", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '3')
        self.assertEqual(self.result['msg'], '短信验证码错误')

    def test_login5(self):
        ''' 空格+正确验证码，空格在开头 '''

        self.req = {"mobile": "13321155433", "code": " "+self.smscode, "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')
        self.assertEqual(self.result['data']['user_info']['userName'], '13321155433')

    def test_login6(self):
        ''' 空格+正确验证码，空格在中间 '''

        self.req = {"mobile": "13321155433", "code": "108 335", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')
        self.assertEqual(self.result['data']['user_info']['userName'], '13321155433')

    def test_login7(self):
        ''' 空格+正确验证码，空格在末尾 '''

        self.req = {"mobile": "13321155433", "code": self.smscode+" ", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')
        self.assertEqual(self.result['data']['user_info']['userName'], '13321155433')

    def test_login8(self):
        ''' 验证码含有英文 '''

        self.req = {"mobile": "13321155433", "code": "iscode", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '3')
        self.assertEqual(self.result['msg'], '短信验证码错误')

    def test_login9(self):
        ''' 验证码含有特殊字符 '''

        self.req = {"mobile": "13321155433", "code": "!@#$%^&*", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '3')
        self.assertEqual(self.result['msg'], '短信验证码错误')

    def test_login10(self):
        ''' 验证码含有html标签 '''

        self.req = {"mobile": "13321155433", "code": "<script></script>", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '3')
        self.assertEqual(self.result['msg'], '短信验证码错误')

    def test_login11(self):
        ''' 验证码含有JS函数 '''

        self.req = {"mobile": "13321155433", "code": "<script>alert(\"hello\")</script>", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '3')
        self.assertEqual(self.result['msg'], '短信验证码错误')

    def test_login12(self):
        ''' 验证码含有敏感词 '''

        self.req = {"mobile": "13321155433", "code": "习近平", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '3')
        self.assertEqual(self.result['msg'], '短信验证码错误')


if __name__ == '__main__':
    # unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    tests = []
    i = 0
    while i <= 12:  #跟测试案例最后一个数字一致，增加案例，这里就要改
        tests.append(LoginBySMSCodeTest("test_login%d" %i))
        i += 1

    print(tests)
    suite.addTests(tests)

    runner = unittest.TextTestRunner()
    runner.run(suite)
