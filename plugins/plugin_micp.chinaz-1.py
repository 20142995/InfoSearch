import requests
from lxml import etree

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'micp.chinaz-1',
        'type': ['domain',],
        'desc': 'icp备案'
    }
    return _info


def execute(target):

    headers = {
        'Host': 'micp.chinaz.com',
        # 'Content-Length': '27',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://micp.chinaz.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://micp.chinaz.com/',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Priority': 'u=0, i',
    }

    data = {
        'keyword': target,
        'accessmode': '2',
    }

    r = requests.post(f'https://micp.chinaz.com/{target}', headers=headers, data=data, verify=False)
    html = etree.HTML(r.text)
    info = {}
    info['主办单位'] = html.xpath(
        'string(//td[text()="主办单位："]/following-sibling::td)')
    info['单位性质'] = html.xpath(
        'string(//td[text()="单位性质："]/following-sibling::td)')
    info['备案号'] = html.xpath(
        'string(//td[text()="备案号："]/following-sibling::td)')
    info['网站名称'] = html.xpath(
        'string(//td[text()="网站名称："]/following-sibling::td)')
    info['网站首页'] = html.xpath(
        'string(//td[text()="网站首页："]/following-sibling::td)')
    info['审核时间'] = html.xpath(
        'string(//td[text()="审核时间："]/following-sibling::td)')
    info['最近检测'] = html.xpath(
        'string(//td[text()="最近检测："]/following-sibling::td)')
    return [info,]


if __name__ == '__main__':
    target = 'xp.cn'
    print(execute(target))
