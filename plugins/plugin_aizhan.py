import requests
from lxml import etree

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'aizhan',
        'type': ['domain'],
        'desc': '网站权重'
    }
    return _info


def execute(target):

    headers = {
        'Host': 'www.aizhan.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close',
    }

    r = requests.get(
        f'https://www.aizhan.com/cha/{target}/', headers=headers, verify=False)
    html = etree.HTML(r.text)
    info = {}
    for table in html.xpath('//table[.//text()="SEO信息"]'):
        for li in table.xpath('tr[2]/td/ul/li'):
            name = ''.join(li.xpath('text()')).rstrip('：')
            rank = ''.join(li.xpath('a/img/@alt'))
            info[name] = rank
    return [info,]


if __name__ == '__main__':
    target = 'google.com'
    print(execute(target))
