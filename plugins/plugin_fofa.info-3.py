import requests
from lxml import etree
from urllib.parse import quote
import base64
import re

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'fofa-3',
        'type': ['ipv4'],
        'desc': ['资产测绘']
    }
    return _info


def execute(target):
    headers = {
        'Host': 'fofa.info',
        'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://fofa.info/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close',
    }
    q = f'ip="{target}"'
    qbase64 = quote(base64.b64encode(q.encode('utf8')).decode())
    params = {
        'qbase64': qbase64,
    }

    r = requests.get('https://fofa.info/result', params=params,
                     headers=headers, verify=False)
    html = etree.HTML(r.text)

    divs = html.xpath(
        '//div[@class="hsxa-clearfix hsxa-meta-data-list-revision-lv1"]')
    result = []
    title = ['host', 'port', 'protocol']
    for div in divs:
        row = [div.xpath('string(.//span[@class="hsxa-host"])').strip(), div.xpath(
            'string(.//a[@class="hsxa-port"])').strip(), re.sub('\s+','',div.xpath('string(.//a[@class="hsxa-protocol"])'))]
        result.append(dict(zip(title, row)))

    return result


if __name__ == '__main__':
    target = '183.230.9.37'
    print(execute(target))
