import requests


def info():
    _info = {
        'name': 'oioweb-1',
        'type': ['ipv4', 'ipv6'],
        'desc': ['归属地']
    }
    return _info


def execute(target):
    api_url = f'https://api.oioweb.cn/api/ip/ipaddress?ip={target}'
    r = requests.get(api_url)
    rj = r.json()
    return [rj.get('result'), ]


if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
