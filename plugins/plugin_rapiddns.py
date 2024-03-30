import requests
from lxml import etree

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'rapiddns',
        'type': ['ipv4'],
        'desc': 'ip反查域名'
    }
    return _info


def execute(target):

    headers = {
        'Host': 'rapiddns.io',
        'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    r = requests.get(f'https://rapiddns.io/s/{target}', headers=headers, verify=False)
    html = etree.HTML(r.text)
    title = html.xpath('//table[.//text()="Domain"]/thead/tr/th/text()')
    result = []
    for tr in html.xpath('//table[.//text()="Domain"]/tbody/tr'):
        row = [td.xpath('string(.)').strip() for td in tr.xpath('td')]
        result.append(dict(zip(title, row)))
    return  result


if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
