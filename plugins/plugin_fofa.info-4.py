import requests

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'fofa-4',
        'type': ['ipv4', 'domain'],
        'desc': '资产测绘'
    }
    return _info


def execute(target):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': '_ga=GA1.1.1790713.1701432210; __fcd=5FLXWKTFZjajbQskduM5Mnwn; Hm_lvt_4275507ba9b9ea6b942c7a3f7c66da90=1711455814,1711461001,1711596290,1711637677; _ga_9GWBD260K9=GS1.1.1711641338.20.0.1711641338.0.0.0',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    rj = requests.get(
        f'https://amap.fofa.info/host/{target}', headers=headers).json()
    results = []
    for item in rj['ports']:
        info = {}
        info['ip'] = rj['ip']
        info['domain'] = rj['domain']
        info.update(item)
        results.append(info)
    return results


if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
