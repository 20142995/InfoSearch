from DrissionPage import ChromiumOptions, ChromiumPage
import time


def info():
    _info = {
        'name': 'aizhan',
        'type': ['domain'],
        'desc': ['权重']
    }
    return _info


def execute(target):
    # co = ChromiumOptions()
    # co.incognito()  # 匿名模式
    # co.headless()  # 无头模式
    # co.set_argument('--no-sandbox')  # 无沙盒模式
    # page = ChromiumPage(co)
    page = ChromiumPage()
    page.get(f'https://www.aizhan.com/cha/{target}/')
    time.sleep(2)
    table = page.ele('xpath://table[.//text()="SEO信息"]')
    info = {}
    for li in table.eles('xpath:tbody/tr[2]/td/ul/li'):
        name = li.ele('xpath:text()').rstrip('：')
        rank = li.ele('xpath:a/img/@alt')
        info[name] = rank
    return [info,]


if __name__ == '__main__':
    target = 'qq.com'
    print(execute(target))
