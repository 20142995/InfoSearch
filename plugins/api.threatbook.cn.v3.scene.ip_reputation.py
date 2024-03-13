import os
import requests


def info():
    _info = {
        'name': 'threatbook-1',
        'type': ['ipv4',],
        'desc': ['IP信誉',]
    }
    return _info


def execute(target):

    url = "https://api.threatbook.cn/v3/scene/ip_reputation"
    apikey = os.getenv('threatbook_key','')
    if apikey:
        query = {
            "apikey":apikey,
            "resource":target,
            "lang":"zh"
        }

        r = requests.get(url, params=query)
        rj = r.json()
        info = rj['data'][target]
    else:
        info = {'msg':'请设置环境变量threatbook_key'}
    return [info,]





if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
