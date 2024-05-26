import requests
from lxml import etree

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'micp.chinaz-2',
        'type': ['domain',],
        'desc': '网安备案'
    }
    return _info


def execute(target):

    headers = {
        'Host': 'micp.chinaz.com',
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
        'Referer': 'https://micp.chinaz.com/psorgan?keyword=cqepc.cn&accessmode=2',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Priority': 'u=0, i',
        # 'Cookie': 'cz_statistics_visitor=8f15372f-fb85-5884-6a9d-da930e56ffa7; toolbox_words=183.230.9.37|183.2.172.42; toolbox_urls=qq.com|8.8.8.8; pinghost=8.8.8.8; Hm_lvt_ca96c3507ee04e182fb6d097cb2a1a4c=1716568694; _clck=1ezjy8r%7C2%7Cfm3%7C0%7C1527; Hm_lpvt_ca96c3507ee04e182fb6d097cb2a1a4c=1716695232; qHistory=Ly9taWNwLmNoaW5hei5jb20vcHNvcmdhbl/nvZHlronlpIfmoYjmn6Xor6Jf56e75YqofC8vbWljcC5jaGluYXouY29tL1/nvZHnq5nlpIfmoYjmn6Xor6Jf56e75YqofC8vd2hvaXMuY2hpbmF6LmNvbS9fV0hPSVPmn6Xor6J8Ly9pY3AuY2hpbmF6LmNvbS9f572R56uZ5aSH5qGI5p+l6K+i; JSESSIONID=E40AF97831943761B02E512A24B1C193; _clsk=1vtcqd3%7C1716697232157%7C5%7C0%7Cv.clarity.ms%2Fcollect',
    }

    params = {
        'keyword': target,
        'accessmode': '2',
    }

    r = requests.get('https://micp.chinaz.com/psorgan', params=params, headers=headers, verify=False)
    html = etree.HTML(r.text)
    info = {}
    info['网站名称'] = html.xpath(
        'string(//td[text()="网站名称"]/following-sibling::td)')
    info['网站域名'] = html.xpath(
        'string(//td[text()="网站域名"]/following-sibling::td)')
    info['开办主体'] = html.xpath(
        'string(//td[text()="开办主体"]/following-sibling::td)')
    info['网站类别'] = html.xpath(
        'string(//td[text()="网站类别"]/following-sibling::td)')
    return [info,]


if __name__ == '__main__':
    target = 'qq.com'
    print(execute(target))
