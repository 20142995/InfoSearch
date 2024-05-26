import os
import execjs
from curl_cffi import requests

def info():
    _info = {
        'name': 'icp.chinaz-1',
        'type': ['domain',],
        'desc': 'icp备案'
    }
    return _info

def execute(target):
    headers = {
        'Host': 'icp.chinaz.com',
        # 'Content-Length': '20',
        'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
        # 'Rd': '521',
        # 'Ts': '1716568712164',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        # 'Token': '1282c9df85c4c78b6ea0b0341891ec89',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://icp.chinaz.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://icp.chinaz.com/qq.com',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Priority': 'u=1, i',
    }
    json_data = {
        'keyword': target,
    }
    # update Rd + Ts + Token + ja3
    js_path = None
    for file in ['./generatetoken.js','./plugins/generatetoken.js']:
        if os.path.exists(file):
            js_path = file
            break
    ctx = execjs.compile(open(js_path, 'r', encoding='utf8').read())
    headers.update(ctx.call('gen_headers', json_data))
    headers = {k:str(v) for k,v in headers.items()}
    r = requests.post('https://icp.chinaz.com/index/api/queryPermit', headers=headers, json=json_data)
    rj = r.json()
    if rj.get('data'):
        return [{"ICP备案号":rj.get('data',rj.get('msg'))}, ]
    else:
        print(f"{rj.get('msg')}")
        return []


if __name__ == '__main__':
    target = 'qq1.com'
    print(execute(target))
