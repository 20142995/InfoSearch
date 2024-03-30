import requests

requests.packages.urllib3.disable_warnings()

def info():
    _info = {
        'name': 'dnslytics',
        'type': ['ipv4',],
        'desc': 'ip反查域名'
    }
    return _info


def execute(target):
    headers = {
        'Host': 'a.dnslytics.com',
        # 'Content-Length': '35',
        'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'https://search.dnslytics.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    json_data = {
        'q': target,
        'dataset': 'ip',
    }

    r = requests.post('https://a.dnslytics.com/v1/report/ip', headers=headers, json=json_data, verify=False)
    if r.status_code == 403:
        '''留坑 5s盾暂时不会绕'''
        return []
    rj = r.json()
    return rj['ip']['domains']



if __name__ == '__main__':
    target = '110.75.129.5'
    print(execute(target))
