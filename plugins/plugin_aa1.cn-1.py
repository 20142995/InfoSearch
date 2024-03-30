import requests

requests.packages.urllib3.disable_warnings()

def info():
    _info = {
        'name': 'aa1.cn-1',
        'type': ['domain','url'],
        'desc': 'icp备案',
    }
    return _info


def execute(target):
    '''有次数限制'''
    headers = {
        'Host': 'v.api.aa1.cn',
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

    r = requests.get(f'https://v.api.aa1.cn/api/icp/index.php?url={target}', headers=headers, verify=False)
    if r.status_code != 200:
        return []
    return r.json()


if __name__ == '__main__':
    target = 'qq.com'
    print(execute(target))
