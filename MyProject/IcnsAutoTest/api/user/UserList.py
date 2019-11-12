import requests
import unittest
import json


class UserList(unittest.TestCase):
    ''' 测试用户列表接口：/api/user/power/user_list '''

    def setUp(self):
        self.url = 'https://testcns.xiudream.com/api/user/power/user_list'
        self.headers = {'Content-Type': 'application/raw'}
        self.cookies = self.login()
    
    def tearDown(self):
        print("响应数据：%s" % self.result)
        
    
    def login(self):
        ''' 先登录获取cookie '''

        req = {"password": "1234qwer", "username": "18612136611", "login_type": 2}
        rsp = requests.post(url='https://testcns.xiudream.com/api/user/login/login_by_password', data=json.dumps(req), headers=self.headers)
        cookies = rsp.cookies.get_dict()  #获取cookie
        result = rsp.json()
        self.assertEqual(result['code'], '0')
        return cookies

    def test_list0(self):
        ''' 查询条件均为空：部门、花名、角色 '''

        # cookies = self.login()  #这里用 UserList.login() 会报错
        self.req = {"departmentId":"","aliasName":"","roleId":"","pageInfo":{"pageNum":1,"pageSize":10},"name":""}
        rsp = requests.post(self.url, cookies=self.cookies, data=json.dumps(self.req), headers=self.headers)
        self.result = rsp.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')
        self.assertEqual(self.result['data']['list'][0]['aliasName'], '超管花名')  #这里因为list是个数组，所以需要用下标取值



if __name__ == "__main__":

    
    suite = unittest.TestSuite()
    tests = []
    i = 0
    while i <= 0:
        tests.append(UserList("test_list%d" %i))
        i += 1

    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)