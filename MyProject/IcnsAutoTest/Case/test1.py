import unittest
import requests
import json
"""
登录接口
"""
url = 'https://testcns.xiudream.com/api/user/login/login_by_password'

# data = json.loads('{"password":"1234qwer","username":"ytroot","login_type":2}')
data = {"password":"1234qwer","username":"ytroot","login_type":2}
r = requests.post(url,headers={ 'Content-Type': 'application/raw'}, data=json.dumps(data))  # 返回的是Json格式的数据
result = r.json()  # Json转成字典
# print(result)
# print(result['data']['token'])
# print(type(result['code']))
assert result['code'] == '0'
assert (result['data']['user_info']['cnName']) == '云天'
 # result['code'] == 0
# assert result['msg'] == 'success'
# assert result['data']['user_info']['cnName'] == '云天'



