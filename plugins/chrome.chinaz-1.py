from DrissionPage import ChromiumOptions, ChromiumPage
import time


def info():
    _info = {
        'name': 'chinaz-1',
        'type': ['url', 'domain', 'icp', 'company_name'],
        'desc': ['ICP备案']
    }
    return _info


def execute(target,debug=False):
    co = ChromiumOptions()
    if not debug:
        co.headless()
    page = ChromiumPage(co)
    page.get('https://icp.chinaz.com/')
    page.ele('@placeholder=请输入网址, 备案号或公司全称').input(target)
    page.ele('@value=立即查询').click()
    time.sleep(2)
    info = {}
    info['主办单位名称'] = page.ele(
        'xpath://td[text()="主办单位名称"]/following-sibling::td/a/text()')
    info['主办单位性质'] = page.ele(
        'xpath://td[text()="主办单位性质"]/following-sibling::td/text()')
    info['ICP备案/许可证号'] = page.ele(
        'xpath://td[text()="ICP备案/许可证号"]/following-sibling::td/span/span/text()')
    info['审核日期'] = page.ele(
        'xpath://td[text()="审核日期"]/following-sibling::td/text()')
    info['网站名称'] = page.ele(
        'xpath://td[text()="网站名称"]/following-sibling::td/text()')
    info['网站首页网址'] = page.ele(
        'xpath://td[text()="网站首页网址"]/following-sibling::td/span/text()')
    info['域名过期时间'] = page.ele(
        'xpath://td[text()="域名过期时间"]/following-sibling::td/span/span/text()')

    return [info,]


if __name__ == '__main__':
    target = 'https://icp.chinaz.com/'
    print(execute(target,debug=True))
