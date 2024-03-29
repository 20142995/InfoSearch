import requests
from lxml import etree

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'ip138-1',
        'type': ['domain',],
        'desc': ['子域名采集']
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
        f'https://site.ip138.com/{target}/domain.htm', headers=headers, verify=False)
    html = etree.HTML(r.text)
    return [{'subdomain': subdomain} for subdomain in html.xpath('//div[@id="J_subdomain"]/p/a/text()')]


if __name__ == '__main__':
    target = 'xx.cn'
    print(execute(target))
