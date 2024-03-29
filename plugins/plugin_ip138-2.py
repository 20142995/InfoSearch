import requests
from lxml import etree

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'ip138_2',
        'type': ['ip', 'domain',],
        'desc': ['ip反查域名', '域名历史解析']
    }
    return _info


def execute(target):
    headers = {
        'Host': 'site.ip138.com',
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
        'Referer': 'https://site.ip138.com/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close',
    }

    r = requests.get(
        f'https://site.ip138.com/{target}/', headers=headers, verify=False)
    html = etree.HTML(r.text)
    ps = html.xpath('//div[@id="J_ip_history"]/p')
    result = []
    title1 = ['ip', 'date']
    for p in ps:
        row = p.xpath('a/text()') + p.xpath('span/text()')
        result.append(dict(zip(title1, row)))
    lis = html.xpath('//ul[.//text()="绑定过的域名如下："]/li')
    result = []
    title2 = ['domain', 'date']
    for li in lis[2:]:
        row = li.xpath('a/text()') + li.xpath('span/text()')
        result.append(dict(zip(title2, row)))

    return result


if __name__ == '__main__':
    target = '9.9.9.9'
    print(execute(target))
