import re
import requests
from lxml import etree

requests.packages.urllib3.disable_warnings()

def info():
    _info = {
        'name': 'beianx',
        'type': ['domain', 'icp', 'company_name'],
        'desc': 'icp备案'
    }
    return _info

def get_acw_sc__v2(arg,key='3000176000856006061501533003690027800375'):
    indexes = [0xf, 0x23, 0x1d, 0x18, 0x21, 0x10, 0x1, 0x26, 0xa, 0x9, 0x13, 0x1f, 0x28, 0x1b, 0x16, 0x17, 0x19, 0xd, 0x6, 0xb, 0x27, 0x12, 0x14, 0x8, 0xe, 0x15, 0x20, 0x1a, 0x2, 0x1e, 0x7, 0x4, 0x11, 0x5, 0x3, 0x1c, 0x22, 0x25, 0xc, 0x24]
    result1 = [''] * 40
    for index in range(len(arg)):
        character = arg[index]
        for i in range(len(indexes)):
            if indexes[i] == index + 1:
                result1[i] = character
    arg1 = ''.join(result1)
    result2 = ''
    index = 0
    while index < len(arg1) and index < len(key):
        hex_num_arg1 = int(arg1[index:index + 2], 16)
        hex_num_key = int(key[index:index + 2], 16)
        xor_result = hex(hex_num_arg1 ^ hex_num_key)[2:]
        xor_result = '0' + xor_result if len(xor_result) == 1 else xor_result
        result2 += xor_result
        index += 2
    return result2

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
        acw_sc__v2 = get_acw_sc__v2(arg1)
        cookies['acw_sc__v2'] = acw_sc__v2
        print(f"{acw_sc__v2=}")
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
    target = 'xp.cn'
    print(execute(target))