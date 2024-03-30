import os
import requests

requests.packages.urllib3.disable_warnings()

def info():
    _info = {
        'name': 'threatbook',
        'type': ['ipv4',],
        'desc': 'ip信誉',
    }
    return _info


def execute(target):

    url = "https://api.threatbook.cn/v3/scene/ip_reputation"
    apikey = os.getenv('threatbook_key', '')
    result = []
    if apikey:
        query = {
            "apikey": apikey,
            "resource": target,
            "lang": "zh"
        }

        r = requests.get(url, params=query)
        rj = r.json()
        info = rj['data'][target]
        result.append(info)
    else:
        print('请设置环境变量threatbook_key')
    return result


if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
