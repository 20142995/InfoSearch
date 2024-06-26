import requests
from lxml import etree

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'shodan',
        'type': ['ipv4',],
        'desc': '资产测绘',
    }
    return _info


def execute(target):
    headers = {
        'Host': 'www.shodan.io',
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
        'Connection': 'close',
    }

    r = requests.get(f'https://www.shodan.io/host/{target}', headers=headers, verify=False)
    html = etree.HTML(r.text)
    title = ['port','protocol']
    result = []
    for port in html.xpath('//h6[@class="grid-heading" and @id]/span'):

        row = [i.strip() for i in port.xpath('string(.)').split('/')]
        result.append(dict(zip(title, row)))

    return result


if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
