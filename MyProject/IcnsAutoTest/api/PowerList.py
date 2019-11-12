import requests
import unittest
import json


class PowerList(unittest.TestCase):
    ''' 测试权限列表接口：/api/user/power/power_list '''

    def setUp(self):
        self.url = 'https://testcns.xiudream.com/api/user/power/power_list'
        self.headers = {'Content-Type': 'application/raw'}
        self.cookies = self.login()
    
    def tearDown(self):
        print("响应数据：%s" % self.result)
        
    
    def login(self):
        ''' 先登录获取cookie '''

        req = {"password": "1234qwer", "username": "ytroot", "login_type": 2}
        rsp = requests.post(url='https://testcns.xiudream.com/api/user/login/login_by_password', data=json.dumps(req), headers=self.headers)
        cookies = rsp.cookies.get_dict()  #获取cookie
        result = rsp.json()
        self.assertEqual(result['code'], '0')
        return cookies

    def test_list0(self):
        ''' 请求 power_list 接口，返回成功 '''

        self.req = {}
        rsp = requests.post(self.url, cookies=self.cookies, data=json.dumps(self.req), headers=self.headers)
        self.result = rsp.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')
        ''' 对管理员角色的返回值进行断言：对城市列表数量、对权限数量、对左侧导航栏 '''
        self.assertEqual(len(self.result['data']['city_list']), 388)      #388个城市
        self.assertEqual(len(self.result['data']['power_id_array']), 84)  #管理员目前有所有权限，目前是84个
        self.assertEqual(self.result['data']['power_tree'][0]['moduleId'], 1)  
        self.assertEqual(self.result['data']['power_tree'][1]['moduleId'], 3)  
        self.assertEqual(self.result['data']['power_tree'][2]['moduleId'], 17)  
        self.assertEqual(self.result['data']['power_tree'][3]['moduleId'], 34)  
        self.assertEqual(self.result['data']['power_tree'][4]['moduleId'], 51)  
        self.assertEqual(self.result['data']['power_tree'][5]['moduleId'], 74)  


if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = []
    i = 0
    while i <= 0:
        tests.append(PowerList("test_list%d" %i))
        i += 1

    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)