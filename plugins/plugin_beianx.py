import requests
import re
import execjs
import base64
from lxml import etree

requests.packages.urllib3.disable_warnings()
jsb64 =  '''U3RyaW5nWydwcm90b3R5cGUnXVsnaGV4WG9yJ10gPSBmdW5jdGlvbihfMHg0ZTA4ZDgpIHsNCiAgICB2YXIgXzB4NWE1ZDNiID0gJyc7DQogICAgZm9yICh2YXIgXzB4ZTg5NTg4ID0gMHgwOyBfMHhlODk1ODggPCB0aGlzWydsZW5ndGgnXSAmJiBfMHhlODk1ODggPCBfMHg0ZTA4ZDhbJ2xlbmd0aCddOyBfMHhlODk1ODggKz0gMHgyKSB7DQogICAgICAgIHZhciBfMHg0MDFhZjEgPSBwYXJzZUludCh0aGlzWydzbGljZSddKF8weGU4OTU4OCwgXzB4ZTg5NTg4ICsgMHgyKSwgMHgxMCk7DQogICAgICAgIHZhciBfMHgxMDVmNTkgPSBwYXJzZUludChfMHg0ZTA4ZDhbJ3NsaWNlJ10oXzB4ZTg5NTg4LCBfMHhlODk1ODggKyAweDIpLCAweDEwKTsNCiAgICAgICAgdmFyIF8weDE4OWUyYyA9IChfMHg0MDFhZjEgXiBfMHgxMDVmNTkpWyd0b1N0cmluZyddKDB4MTApOw0KICAgICAgICBpZiAoXzB4MTg5ZTJjWydsZW5ndGgnXSA9PSAweDEpIHsNCiAgICAgICAgICAgIF8weDE4OWUyYyA9ICdceDMwJyArIF8weDE4OWUyYzsNCiAgICAgICAgfQ0KICAgICAgICBfMHg1YTVkM2IgKz0gXzB4MTg5ZTJjOw0KICAgIH0NCiAgICByZXR1cm4gXzB4NWE1ZDNiOw0KfQ0KOw0KU3RyaW5nWydwcm90b3R5cGUnXVsndW5zYm94J10gPSBmdW5jdGlvbigpIHsNCiAgICB2YXIgXzB4NGIwODJiID0gWzB4ZiwgMHgyMywgMHgxZCwgMHgxOCwgMHgyMSwgMHgxMCwgMHgxLCAweDI2LCAweGEsIDB4OSwgMHgxMywgMHgxZiwgMHgyOCwgMHgxYiwgMHgxNiwgMHgxNywgMHgxOSwgMHhkLCAweDYsIDB4YiwgMHgyNywgMHgxMiwgMHgxNCwgMHg4LCAweGUsIDB4MTUsIDB4MjAsIDB4MWEsIDB4MiwgMHgxZSwgMHg3LCAweDQsIDB4MTEsIDB4NSwgMHgzLCAweDFjLCAweDIyLCAweDI1LCAweGMsIDB4MjRdOw0KICAgIHZhciBfMHg0ZGEwZGMgPSBbXTsNCiAgICB2YXIgXzB4MTI2MDVlID0gJyc7DQogICAgZm9yICh2YXIgXzB4MjBhN2JmID0gMHgwOyBfMHgyMGE3YmYgPCB0aGlzWydceDZjXHg2NVx4NmVceDY3XHg3NFx4NjgnXTsgXzB4MjBhN2JmKyspIHsNCiAgICAgICAgdmFyIF8weDM4NWVlMyA9IHRoaXNbXzB4MjBhN2JmXTsNCiAgICAgICAgZm9yICh2YXIgXzB4MjE3NzIxID0gMHgwOyBfMHgyMTc3MjEgPCBfMHg0YjA4MmJbJ2xlbmd0aCddOyBfMHgyMTc3MjErKykgew0KICAgICAgICAgICAgaWYgKF8weDRiMDgyYltfMHgyMTc3MjFdID09IF8weDIwYTdiZiArIDB4MSkgew0KICAgICAgICAgICAgICAgIF8weDRkYTBkY1tfMHgyMTc3MjFdID0gXzB4Mzg1ZWUzOw0KICAgICAgICAgICAgfQ0KICAgICAgICB9DQogICAgfQ0KICAgIF8weDEyNjA1ZSA9IF8weDRkYTBkY1snXHg2YVx4NmZceDY5XHg2ZSddKCcnKTsNCiAgICByZXR1cm4gXzB4MTI2MDVlOw0KfQ0KOw0KZnVuY3Rpb24gZ2VuX2FyZzIoYXJnMSl7DQogICAgLy8gYXJnMSA9ICJDQ0E1RTk1QUIxQ0U3NzU5QzQ5MEY4QkY0QjI2RkQzQ0E1NUM1MTYwIg0KICAgIHZhciBfMHgyM2EzOTIgPSBhcmcxWyd1bnNib3gnXSgpOw0KICAgIGFyZzIgPSBfMHgyM2EzOTJbJ2hleFhvciddKCczMDAwMTc2MDAwODU2MDA2MDYxNTAxNTMzMDAzNjkwMDI3ODAwMzc1Jyk7DQogICAgcmV0dXJuIGFyZzINCn07'''

def info():
    _info = {
        'name': 'beianx',
        'type': ['domain', 'icp', 'company_name'],
        'desc': ['icp备案']
    }
    return _info

def execute(target):
    headers = {
        'Host': 'www.beianx.cn',
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

    r = requests.get(f'https://www.beianx.cn/search/{target}', headers=headers, verify=False)
    cookies = r.cookies.get_dict()
    arg1 = re.findall("var arg1='(.*?)';",r.text)
    if arg1:
        arg1 = arg1[0]
        arg2 = execjs.compile(base64.b64decode(jsb64).decode('utf8')).call('gen_arg2',arg1)
        cookies['acw_sc__v2'] = arg2
        r = requests.get(f'https://www.beianx.cn/search/{target}', headers=headers,cookies=cookies, verify=False)
    html = etree.HTML(r.text)
    result = []
    for table in html.xpath('//table[.//text()="序号"]'):
        title = table.xpath('thead/tr/th/text()')
        title = [i.strip() for i in title]
        for tr in table.xpath('tr'):
            row = [td.xpath('string(.)').strip() for td in tr.xpath('td')]
            result.append(dict(zip(title, row)))
    return result

if __name__ == '__main__':
    target = 'qq.com'
    print(execute(target))