from DrissionPage import ChromiumOptions, ChromiumPage
import time


def info():
    _info = {
        'name': 'chinaz-2',
        'type': ['ipv4', 'domain'],
        'desc': ['归属地']
    }
    return _info


def execute(target,debug=False):
    co = ChromiumOptions()
    if not debug:
        co.headless()
    page = ChromiumPage(co)
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
    print(execute(target,debug=True))
