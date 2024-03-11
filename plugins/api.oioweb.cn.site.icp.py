import requests


def info():
    _info = {
        'name': 'oioweb',
        'type': ['domain',],
        'desc': ['ICP备案']
    }
    return _info


def execute(target):
    api_url = f'https://api.oioweb.cn/api/site/icp?domain={target}'
    r = requests.get(api_url)
    rj = r.json()
    return [rj.get('result'), ]


if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
