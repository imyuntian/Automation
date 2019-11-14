import requests
import unittest
import json


class PublicSeaSearchHotel(unittest.TestCase):
    ''' 测试公海搜索酒店接口 '''

    def setUp(self):
        self.url = 'https://testcns.xiudream.com/api/customer/public_sea/search_hotel'
        self.headers = {'Content-Type': 'application/raw'}
        self.cookies = self.login()
    
    clanum = 1
    def tearDown(self):
        print("\t用例%02d的响应数据：%s" % (PublicSeaSearchHotel.clanum, self.result))
        PublicSeaSearchHotel.clanum += 1

    def login(self):
        ''' 先登录获取cookie '''
        req = {"password": "1234qwer", "username": "ytroot", "login_type": 2}
        rsp = requests.post(url='https://testcns.xiudream.com/api/user/login/login_by_password', data=json.dumps(req), headers=self.headers)
        cookies = rsp.cookies.get_dict()  #获取cookie
        result = rsp.json()
        self.assertEqual(result['code'], '0')
        return cookies

    def test_1_list(self):
        ''' 请求成功 '''
        rsp = requests.get(self.url, cookies=self.cookies)
        self.result = rsp.json()
        self.assertEqual(self.result['code'], '0')
        self.assertEqual(self.result['msg'], 'success')
        self.assertEqual(self.result['data']['pageInfo']['total'], 1151183)



if __name__ == "__main__":
    suite = unittest.TestSuite()
    tests = []
    i = 1
    while i <= 1:  #跟测试案例最后一个数字一致，增加案例，这里就要改
        tests.append(PublicSeaSearchHotel("test_%d_list" %i))
        i += 1

    suite.addTests(tests)
    runner = unittest.TextTestRunner()
    runner.run(suite)