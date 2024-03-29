import requests

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'icp.chinaz-1',
        'type': ['domain',],
        'desc': ['icp备案']
    }
    return _info


def execute(target):
    headers = {
        'Host': 'icp.chinaz.com',
        # 'Content-Length': '22',
        'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://icp.chinaz.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://icp.chinaz.com',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    json_data = {
        'keyword': target,
    }

    r = requests.post('https://icp.chinaz.com/index/api/queryPermit', headers=headers, json=json_data, verify=False)
    rj = r.json()
    return [{"ICP备案号":rj.get('data')}, ]


if __name__ == '__main__':
    target = 'qq.com'
    print(execute(target))
