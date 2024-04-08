import requests
import re

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'tool.chinaz-1',
        'type': ['host:port',],
        'desc': '端口检测'
    }
    return _info


def execute(target):
    headers = {
        'Host': 'tool.chinaz.com',
        # 'Content-Length': '21',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://tool.chinaz.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://tool.chinaz.com/port',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Priority': 'u=0, i',
    }
    if ':' not in target:
        return []
    host,port = target.split(':')
    data = {
        'host': host,
        'port': port,
    }

    r1 = requests.post('https://tool.chinaz.com/port', headers=headers, data=data, verify=False)
    token = re.findall('id="token" value="(.*?)"',r1.text)
    ts = re.findall('id="ts" value="(.*?)"',r1.text)
    if not token or not ts:
        return []
    headers = {
        'Host': 'tool.chinaz.com',
        # 'Content-Length': '94',
        'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://tool.chinaz.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://tool.chinaz.com/port',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Priority': 'u=1, i',
    }

    json_data = {
        'host': host,
        'port': port,
        'ts': ts[0],
        'token': token[0],
    }

    rj2 = requests.post('https://tool.chinaz.com/scanport', headers=headers, json=json_data, verify=False).json()
    return [{'isOpen':rj2['data']['isOpen']},]


if __name__ == '__main__':
    target = 'qq.com:80'
    print(execute(target))
