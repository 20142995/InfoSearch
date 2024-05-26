import re
import requests
from lxml import etree

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'whois.chinaz',
        'type': ['domain',],
        'desc': 'whois',
    }
    return _info


def execute(target):
    headers = {
        'Host': 'whois.chinaz.com',
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
        'Referer': 'https://whois.chinaz.com',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Priority': 'u=0, i',
    }

    r = requests.get(f'https://whois.chinaz.com/{target}', headers=headers, verify=False)
    # print(r.text)
    html = etree.HTML(r.text)
    info = {}
    for div in html.xpath("//div[@description-item]"):
        key = div.xpath("string(div[@item-label])").strip()
        value = re.sub('\s+',' ',div.xpath("string(div[@item-value])").strip())
        if key not in ['域名','注册商','注册商服务器','注册商电话','更新时间','注册时间','过期时间','域名年龄','DNS']:continue
        info[key] = value
    if info:
        return [info]
    else:
        return []


if __name__ == '__main__':
    target = 'qq.com'
    print(execute(target))
