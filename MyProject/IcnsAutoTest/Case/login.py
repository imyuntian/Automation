import requests
import unittest
import json

class LoginByPasswordTest(unittest.TestCase):
    ''' 测试【通过密码登录】接口：login_by_password '''

    def setUp(self):
        self.url = 'https://testcns.xiudream.com/api/user/login/login_by_password'
        self.headers = {'Content-Type': 'application/raw'}
        self.data = {"password": "1234qwer", "username": "ytroot", "login_type": 2}

    def tearDown(self):
        print("响应数据：%s" %self.result)

    def test_login_success(self):
        ''' 登录成功 '''
        r = requests.post(self.url, headers = self.headers, data = json.dumps(self.data))
        self.result = r.json()
        self.assertEqual(self.result['code'],'0')
        self.assertEqual(self.result['msg'],'success')


if __name__ == '__main__':
    unittest.main()