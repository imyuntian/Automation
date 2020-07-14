import configparser
import json
import os
import requests


def get_url():
    apicfg_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/conf/api.ini'
    apicfg = configparser.ConfigParser()
    apicfg.read(apicfg_path)
    url = apicfg.get('apiconf', 'testSendPo')
    return url


def get_header():
    header = {'Content-Type': 'application/json'}
    return header


def get_body():
    with open('../../data/po.json', 'rt', encoding='utf-8') as fp:
        # 返回一个字典
        dict_data = json.load(fp)
        # 转成json
        json_data = json.dumps(dict_data, ensure_ascii=False)
        print(json_data)
    return json_data


def send(url, header, body):
    print(body)
    requests.post(url=url, data=body.encode('utf-8'), headers=header)


if __name__ == '__main__':
    str_url = get_url()
    str_header = get_header()
    str_body = get_body()
    send(str_url, str_header, str_body)



