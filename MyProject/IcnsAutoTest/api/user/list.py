import requests
import unittest
import json
''' 暂时放放 '''

class List(unittest.TestCase):
    '''  '''

    def setUp(self):
        self.url = 'https://testcns.xiudream.com/crm/department/list'
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
        ''' 模拟选中左侧导航栏 开发-南京的情况 '''

        self.req = {"departmentId":4,"pageInfo":{"pageNum":1,"pageSize":10}}
        rsp = requests.post(self.url, cookies=self.cookies, data=json.dumps(self.req), headers=self.headers)
        self.result = rsp.json()
        print(self.result)
        # self.assertEqual(self.result['code'], '0')
        # self.assertEqual(self.result['msg'], 'success')
        



if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = []
    i = 0
    while i <= 0:
        tests.append(List("test_list%d" %i))
        i += 1

    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)