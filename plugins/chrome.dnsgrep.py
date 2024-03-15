from DrissionPage import ChromiumOptions, ChromiumPage
import time


def info():
    _info = {
        'name': 'dnsgrep',
        'type': ['ipv4',],
        'desc': ['IP反查域名']
    }
    return _info


def execute(target,debug=False):
    co = ChromiumOptions()
    co.incognito()
    if not debug:
        co.headless()
    page = ChromiumPage(co)
    page.get(f'https://www.dnsgrep.cn/ip/{target}')
    time.sleep(5)
    trs = page.eles('xpath://table[.//text()="域名"]/tbody/tr')
    result = []
    title = trs[0].eles('xpath:th/text()')
    for tr in trs[1:]:
        row = [i.texts()[0].strip() for i in tr.eles('xpath:td')]
        result.append(dict(zip(title, row)))

    return result


if __name__ == '__main__':
    target = '110.75.129.5'
    print(execute(target))
