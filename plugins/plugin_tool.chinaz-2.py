import requests
import re
from lxml import etree

requests.packages.urllib3.disable_warnings()

def info():
    _info = {
        'name': 'tool.chinaz-2',
        'type': ['domain', 'url',],
        'desc': 'HTTP状态'
    }
    return _info

def execute(target):
    headers = {
        'Host': 'tool.chinaz.com',
        'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://tool.chinaz.com/pagestatus/',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Priority': 'u=0, i',
    }

    params = {
        'url': target,
    }

    response = requests.get('https://tool.chinaz.com/pagestatus/', params=params, headers=headers, verify=False)
    html = etree.HTML(response.text)
    result = []
    for ul in html.xpath('//ul[.//text()="检测结果"]'):
        lis = ul.xpath('li')
        info = {}
        for li in lis[1:]:
            k = li.xpath('string(div[1])').strip()
            v = li.xpath('string(div[2])').strip()
            info[k] = v
        result.append(info)
    return result

if __name__ == '__main__':
    target = 'qq.com'
    print(execute(target))