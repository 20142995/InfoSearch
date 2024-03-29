import requests

requests.packages.urllib3.disable_warnings()

def info():
    _info = {
        'name': 'webscan',
        'type': ['ipv4',],
        'desc': ['ip反查域名']
    }
    return _info


def execute(target):
    api_url = f'https://api.webscan.cc/?action=query&ip={target}'
    r = requests.get(api_url)
    rj = r.json()
    if not rj:
        rj = []
    return rj


if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
