import requests
from lxml import etree

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'pearktrue.cn-2',
        'type': ['domain'],
        'desc': 'icp备案',
    }
    return _info


def execute(target):

    headers = {
        'Host': 'api.pearktrue.cn',
        'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close',
    }

    params = {
        'domain':target,
    }
    result = []
    r = requests.get('https://api.pearktrue.cn/api/icp/', params=params, headers=headers, verify=False)
    info = r.json().get('data',{})
    if info:
        result.append(info)
    return result


if __name__ == '__main__':
    target = 'qq.com'
    print(execute(target))
