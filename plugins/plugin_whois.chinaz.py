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
        # 'Content-Length': '11',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://whois.chinaz.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://whois.chinaz.com/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    data = {
        'host': target,
    }

    r = requests.post('https://whois.chinaz.com/qq.com',
                      headers=headers, data=data, verify=False)
    html = etree.HTML(r.text)
    lis = html.xpath('//div[@id="whois_info"]/li')
    result = []
    if lis:
        _info = {}
        for li in lis:
            row = [div.xpath('string(.)').strip() for div in li.xpath('div')]
            _info[';\n'.join(row[:1])] = ';\n'.join(row[1:])
        result.append(_info)
    return result


if __name__ == '__main__':
    target = 'qq.com'
    print(execute(target))
