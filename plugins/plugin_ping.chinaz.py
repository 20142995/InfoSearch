import os
import execjs
import requests
from lxml import etree

requests.packages.urllib3.disable_warnings()

def info():
    _info = {
        'name': 'ping.chinaz',
        'type': ['domain','ipv4'],
        'desc': 'ping检测'
    }
    return _info

def execute(target):
    js_path = None
    for file in ['./generatetoken.js','./plugins/generatetoken.js']:
        if os.path.exists(file):
            js_path = file
            break
    ctx = execjs.compile(open(js_path, 'r', encoding='utf8').read())
    headers = {
        'Host': 'ping.chinaz.com',
        # 'Content-Length': '123',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://ping.chinaz.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://ping.chinaz.com/',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Priority': 'u=0, i',
    }

    data = {
        'host': target,
        'linetype': '电信,多线,联通,移动,其他',
    }
    results = []
    response = requests.post(f'https://ping.chinaz.com/{target}', headers=headers, data=data, verify=False)
    html = etree.HTML(response.text)
    divs = html.xpath('//div[@class="row listw tc clearfix"]')
    for div in divs:
        id = div.xpath('@id')[0]
        token = div.xpath('@token')[0]
        name = div.xpath('div[1]/text()')[0]
        headers = {
            'Host': 'ping.chinaz.com',
            # 'Content-Length': '196',
            'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Origin': 'https://ping.chinaz.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://ping.chinaz.com',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Priority': 'u=4, i',
        }

        params = ctx.call('gen_params',target)
        json_data = {
            'host': target,
            'guid': id,
            'token': token,
            'identify': 0,
        }
        json_data.update(params)
        try:
            rj = requests.post('https://ping.chinaz.com/pingcheck', headers=headers, json=json_data, verify=False).json()
            info = {'name':name}
            info.update(rj['data'])
            results.append(info)
        except:
            pass
        break
    return results
if __name__ == '__main__':
    target = 'qq.com'
    print(execute(target))