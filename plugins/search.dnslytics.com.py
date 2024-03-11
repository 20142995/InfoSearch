from DrissionPage import ChromiumOptions, ChromiumPage
import time


def info():
    _info = {
        'name': 'dnslytics',
        'type': ['ipv4',],
        'desc': ['IP反查域名']
    }
    return _info


def execute(target):
    result = []
    # co = ChromiumOptions()
    # co.incognito()  # 匿名模式
    # co.headless()  # 无头模式
    # co.set_argument('--no-sandbox')  # 无沙盒模式
    # page = ChromiumPage(co)
    page = ChromiumPage()
    page.get(f'https://search.dnslytics.com/ip/{target}')
    time.sleep(2)
    table = page.ele('xpath://table[.//text()="DomainRank"]')
    result = []
    title = [i.texts()[0] for i in table.eles('xpath:thead/tr/th')]
    for tr in table.eles('xpath:tbody/tr'):
        row = [i.texts()[0].strip() for i in tr.eles('xpath:td')]
        result.append(dict(zip(title, row)))
    return result


if __name__ == '__main__':
    target = '110.75.129.5'
    print(execute(target))
