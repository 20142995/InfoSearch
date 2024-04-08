import requests
import base64

requests.packages.urllib3.disable_warnings()

def info():
    _info = {
        'name': 'ti.sangfor',
        'type': ['ipv4',],
        'desc': 'ip信誉',
    }
    return _info


def execute(target):
    session = requests.session()
    headers = {
        'Host': 'ti.sangfor.com.cn',
        # 'Content-Length': '10',
        'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
        'Accept-Language': 'ZH-CN',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Csrftoken': 'token',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://ti.sangfor.com.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ti.sangfor.com.cn/',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Priority': 'u=1, i',
        'Connection': 'close',
    }

    data = {
        'lang': 'ZH-CN',
    }

    session.post('https://ti.sangfor.com.cn/api/v1/language/set_language', headers=headers, data=data, verify=False)
    headers['X-Csrftoken'] = session.cookies.get('csrftoken')
    data = {
        'query': 'OC44LjguOA==',
        'days': '30',
    }

    rj = session.post('https://ti.sangfor.com.cn/api/v1/threats/ioc', headers=headers, data=data, verify=False).json()
    if 'data' in rj:
        return [{'threat_analysis':rj['data']['threat_analysis']['open_intelligence_tags']}]
    else:
        print('次数限制')
        return []



if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
