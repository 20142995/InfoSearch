import requests
import re

requests.packages.urllib3.disable_warnings()

def info():
    _info = {
        'name': 'alexa.cn',
        'type': ['domain',],
        'desc': 'icp备案',
    }
    return _info


def execute(target):
    headers = {
        'Host': 'www.alexa.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close',
    }

    r1 = requests.get(f'http://www.alexa.cn/{target}', headers=headers, verify=False)
    token = re.findall("'#ICP', \{\s+token : '(.*?)'",r1.text,re.S)
    headers = {
        'Host': 'www.alexa.cn',
        # 'Content-Length': '0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://www.alexa.cn',
        'Referer': 'http://www.alexa.cn/qq.com',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close',
        # 'Cookie': 'exi_query_history=vIKMzqc6vDQWiXOi3ms0XphimOtQ6LRSvOrqcwS8gu9IsOYPA3Gzjgc-GBpPI-GNfzzfN7KVNPJmxZwYy-CxF1PdA-M-M',
    }
    if not token:
        return []
    params = {
        'token': token[0],
        'url': target,
        'host': '',
        'vcode': '',
    }

    r2 = requests.post('http://www.alexa.cn/api/icp/info', params=params, headers=headers, verify=False)
    return r2.json()['data']


if __name__ == '__main__':
    target = 'qq.com'
    print(execute(target))
