from DrissionPage import ChromiumOptions, ChromiumPage
import time


def info():
    _info = {
        'name': 'chinaz',
        'type': ['ipv4', 'domain'],
        'desc': ['归属地']
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
    page.get('https://ip.tool.chinaz.com/')
    page.ele('@id=address').input(target)
    page.ele('@value=查询').click()
    time.sleep(2)
    s = page.eles('xpath://span[text()="域名/IP"]/../../div')
    result = []
    title = s[0].eles('xpath:span/text()')
    for div in s[1:]:
        row = []
        row.append(div.ele('xpath:span[1]/text()'))
        row.append(div.ele('xpath:span[2]/text()'))
        row.append(div.ele('xpath:span[3]/text()'))
        row.append(div.ele('xpath:span[4]/text()'))
        row.append(div.ele('xpath:span[6]/em/text()'))
        result.append(dict(zip(title, row)))
    return result


if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
