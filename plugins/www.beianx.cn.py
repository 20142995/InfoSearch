from DrissionPage import ChromiumOptions, ChromiumPage
import time


def info():
    _info = {
        'name': 'beianx',
        'type': ['domain', 'icp', 'company_name'],
        'desc': ['ICP备案']
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
    page.get(f'https://www.beianx.cn/search/{target}')
    time.sleep(2)
    table = page.ele('xpath://table[.//text()="序号"]')
    result = []
    title = table.eles('xpath:thead/tr/th/text()')
    title = [i.strip() for i in title]

    for tr in table.eles('xpath:tbody/tr'):
        td = [i.texts() for i in tr.eles('xpath:td')]
        row = [''.join(i).strip() for i in td]
        result.append(dict(zip(title, row)))
    return result


if __name__ == '__main__':
    target = '北京百度网讯科技有限公司'
    print(execute(target))
