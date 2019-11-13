import requests
import unittest
import json
import os,sys
import configparser as cfgparser

num = 1  #定义一个全局变量，用来做打印自增ID
class LoginByPasswordTest(unittest.TestCase):
    ''' 测试PC端【通过密码登录】接口：login_by_password '''
    # 在测试类的开始时被执行一次
    @classmethod
    def setUpClass(self):
        #构造读取配置文件的路径：d:\mygit\Automation\MyProject\IcnsAutoTest\api\api.ini
        apicfg_path = os.path.dirname(os.path.dirname(__file__))+"\\conf\\api.ini"
        apicf = cfgparser.ConfigParser()
        apicf.read(apicfg_path)
        #换测试环境、测试账号，直接改这一处即可
        self.host = apicf.get("apiconf", "testhost")
        self.user = apicf.get("apiconf", "kfjl")
        self.pwd  = apicf.get("apiconf", "kfjlpwd")


    def setUp(self):
        self.url = self.host + "api/user/login/login_by_password"
        self.headers = {'Content-Type': 'application/raw'}

    clanum = 1  # 定义一个类变量，可以替代全局变量的用法
    def tearDown(self):
        # 使用全局变量时，这里必须加 global 
        global num
        print("\t用例%02d的响应数据：%s" % (num, self.result))
        num += 1

        # 使用类对象代替全局变量
        # print("\t用例%02d的响应数据：%s" % (LoginByPasswordTest.clanum, self.result))
        # LoginByPasswordTest.clanum += 1
        
    def test_1_login(self):
        ''' 登录成功 '''

        self.req = {"password": self.pwd, "username": self.user, "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')
        self.assertEqual(self.result['data']['user_info']['aliasName'], '开发云天5433')

    def test_2_login(self):
        ''' 账号正确，密码错误 '''

        self.req = {"password": "errorpwd1", "username": "18384156109", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '10007')
        self.assertEqual(self.result['msg'], '用户名或密码错误，你还有9机会')

    def test_3_login(self):
        ''' 账号错误，密码正确 '''

        self.req = {"password": "1234qwer", "username": "username2", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '10006')
        self.assertEqual(self.result['msg'], '该帐号无权限登录CNS')

    def test_4_login(self):
        ''' 账号为空 '''

        self.req = {"password": "1234qwer", "username": "", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '1')
        self.assertEqual(self.result['msg'], '参数 username 不能为空')

    def test_5_login(self):
        ''' 密码为空 '''

        self.req = {"password": "", "username": "15198139787", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '1')
        self.assertEqual(self.result['msg'], '参数 password 不能为空')

    def test_6_login(self):
        ''' 账号是一个空格 '''

        self.req = {"password": "1234qwer", "username": " ", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '1')
        self.assertEqual(self.result['msg'], '参数 username 不能为空')

    def test_7_login(self):
        ''' 密码是一个空格 '''

        self.req = {"password": " ", "username": "18328578126", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '1')
        self.assertEqual(self.result['msg'], '参数 password 不能为空')  #后台如果做了去空格，就应返回参数不能为空，而不是把空格识别成密码

    def test_8_login(self):
        ''' 账号是html标签 '''

        self.req = {"password": "1234qwer", "username": "<script></script>", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '10006')
        self.assertEqual(self.result['msg'], '该帐号无权限登录CNS')

    def test_9_login(self):
        ''' 账号是html标签 '''

        self.req = {"password": "<script></script>", "username": "15657169205", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '10007')
        self.assertEqual(self.result['msg'], '用户名或密码错误，你还有9机会')

    def test_10_login(self):
        ''' 账号是JS函数 '''

        self.req = {"password": "1234qwer", "username": "<script>alert(\"hello\")</script>", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '10006')
        self.assertEqual(self.result['msg'], '该帐号无权限登录CNS')

    def test_11_login(self):
        ''' 密码是JS函数 '''

        self.req = {"password": "<script>alert(\"hello\")</script>", "username": "15025316959", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '10007')
        self.assertEqual(self.result['msg'], '用户名或密码错误，你还有9机会')

    def test_12_login(self):
        ''' 密码正确时，账号是超11位手机号 '''

        self.req = {"password": "1234qwer", "username": "133211554330", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        # self.assertEqual(self.result['code'], 'xxxxx')
        self.assertEqual(self.result['msg'], '请输入正确的手机号')

    def test_13_login(self):
        ''' 正确账号开头有空格 '''

        self.req = {"password": "1234qwer", "username": " 13321155433", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')
        
    def test_14_login(self):
        ''' 正确账号中间有空格 '''

        self.req = {"password": "1234qwer", "username": "133211 55433", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')

    def test_15_login(self):
        ''' 正确账号末尾有空格 '''

        self.req = {"password": "1234qwer", "username": "13321155433 ", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')

    def test_16_login(self):
        ''' 简单SQL注入：账号任意，密码输入 'OR'1'='1 '''

        self.req = {"password": "'OR'1'='1", "username": "13321155433 ", "login_type": 2}
        r = requests.post(self.url, data=json.dumps(self.req), headers=self.headers)
        self.result = r.json()
        self.assertEqual(self.result['code'], '10006')
        self.assertEqual(self.result['msg'], '该帐号无权限登录CNS')


if __name__ == '__main__':
    # unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    tests = []
    i = 1
    while i <= 16:  # 跟最后一个测试案例的数字一致，增加案例时，这里要改
        tests.append(LoginByPasswordTest("test_%d_login" % i))
        i += 1

    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)

