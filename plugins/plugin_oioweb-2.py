import requests

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'oioweb-2',
        'type': ['domain',],
        'desc': 'icp备案',
    }
    return _info


def execute(target):
    api_url = f'https://api.oioweb.cn/api/site/icp?domain={target}'
    r = requests.get(api_url)
    return [r.json()['result'], ]


if __name__ == '__main__':
    target = 'baidu.com'
    print(execute(target))
