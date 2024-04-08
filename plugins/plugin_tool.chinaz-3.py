import requests
import re
from lxml import etree

requests.packages.urllib3.disable_warnings()

def info():
    _info = {
        'name': 'tool.chinaz-3',
        'type': ['domain', 'url',],
        'desc': 'HTTP源代码'
    }
    return _info

def execute(target):
    headers = {
        'Host': 'tool.chinaz.com',
        # 'Content-Length': '38',
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
        'Referer': 'https://tool.chinaz.com/tools/pagecode',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Priority': 'u=0, i',
    }

    data = {
        'queryType': '3',
        'showType': '1',
        'queryUrl': target,
    }

    response = requests.post('https://tool.chinaz.com/tools/pagecode', headers=headers, data=data, verify=False)
    html = etree.HTML(response.text)
    htmltext = html.xpath('//*[@id="htmltext"]/text()')
    if not htmltext:
        return []
    return [{'htmltext':htmltext[0]}]

if __name__ == '__main__':
    target = 'qq.com'
    print(execute(target))