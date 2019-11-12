import requests
import unittest
import json


class ToDoTaskList(unittest.TestCase):
    ''' 测试个人工作台待办任务接口 '''

    def setUp(self):
        self.url = 'https://testcns.xiudream.com/api/task/task/to_do_task_list'
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
        ''' 请求成功 '''
        rsp = requests.get(self.url, cookies=self.cookies)
        self.result = rsp.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')
        self.assertEqual(self.result['data']['today'][0]['task_type_str'], '维护任务')
        self.assertEqual(self.result['data']['today'][1]['task_type_str'], '营收任务')
        self.assertEqual(self.result['data']['today'][2]['task_type_str'], '提醒任务')
        self.assertEqual(self.result['data']['yesterday'][0]['task_type_str'], '维护任务')
        self.assertEqual(self.result['data']['yesterday'][1]['task_type_str'], '营收任务')
        self.assertEqual(self.result['data']['yesterday'][2]['task_type_str'], '提醒任务')


if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = []
    i = 0
    while i <= 0:
        tests.append(ToDoTaskList("test_list%d" %i))
        i += 1

    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)