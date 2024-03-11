from DrissionPage import ChromiumOptions, ChromiumPage
import time


def info():
    _info = {
        'name': 'ip138',
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
    page.get(f'https://site.ip138.com/{target}/')
    time.sleep(2)
    lis = page.eles('xpath://ul[.//text()="绑定过的域名如下："]/li')
    result = []
    title = ['domain', 'date']
    for li in lis[2:]:
        row = [li.ele('xpath:a/text()'), li.ele('xpath:span/text()')]
        result.append(dict(zip(title, row)))

    return result


if __name__ == '__main__':
    target = '110.75.129.5'
    print(execute(target))
