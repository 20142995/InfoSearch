from DrissionPage import ChromiumOptions, ChromiumPage
import time


def info():
    _info = {
        'name': 'chinaz-3',
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
    page.get('https://stool.chinaz.com/same')
    page.ele('@placeholder=请输入要查询的IP或域名').input(target)
    page.ele('@value=查询').click()
    time.sleep(3)
    s = page.eles('xpath://ul[.//text()="序号"]/li')
    title = s[0].eles('xpath:div/text()')

    for li in s[1:]:
        row = []
        row.append(li.ele('xpath:div[1]/text()'))
        row.append(li.ele('xpath:div[2]/a/text()'))
        row.append(li.ele('xpath:div[3]/a/text()'))
        row.append(li.ele('xpath:div[4]/a/img/@src')[50:-4] if li.ele('xpath:div[4]/a/img/@src') else '')
        row.append(li.ele('xpath:div[5]/a/text()'))
        result.append(dict(zip(title, row)))
    return result


if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
