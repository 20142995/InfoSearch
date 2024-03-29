import requests
from lxml import etree

requests.packages.urllib3.disable_warnings()


def info():
    _info = {
        'name': 'icp.chinaz-1',
        'type': ['domain','icp','company_name'],
        'desc': ['icp备案']
    }
    return _info


def execute(target):
    headers = {
        'Host': 'icp.chinaz.com',
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
        'Referer': 'https://icp.chinaz.com/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    r = requests.get(
        f'https://icp.chinaz.com/{target}', headers=headers, verify=False)
    html = etree.HTML(r.text)
    info = {}
    info['主办单位名称'] = html.xpath(
        'string(//td[text()="主办单位名称"]/following-sibling::td/a)')
    info['主办单位性质'] = html.xpath(
        'string(//td[text()="主办单位性质"]/following-sibling::td)')
    info['ICP备案/许可证号'] = html.xpath(
        'string(//td[text()="ICP备案/许可证号"]/following-sibling::td/span/span)')
    info['审核日期'] = html.xpath(
        'string(//td[text()="审核日期"]/following-sibling::td)')
    info['网站名称'] = html.xpath(
        'string(//td[text()="网站名称"]/following-sibling::td)')
    info['网站首页网址'] = html.xpath(
        'string(//td[text()="网站首页网址"]/following-sibling::td/span)')
    info['域名过期时间'] = html.xpath(
        'string(//td[text()="域名过期时间"]/following-sibling::td/span/span)')
    return [info,]


if __name__ == '__main__':
    target = '厦门享联科技有限公司'
    print(execute(target))
