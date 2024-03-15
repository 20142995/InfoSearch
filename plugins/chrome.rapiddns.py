from DrissionPage import ChromiumOptions, ChromiumPage
import time


def info():
    _info = {
        'name': 'rapiddns',
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
    page.get(f'https://rapiddns.io/sameip/{target}')
    time.sleep(2)
    table = page.ele('xpath://table[.//text()="Domain"]')
    result = []
    title = table.eles('xpath:thead/tr/th/text()')
    title = [i.strip() for i in title][1:]

    for tr in table.eles('xpath:tbody/tr'):
        td = [i.texts() for i in tr.eles('xpath:td')]
        row = [''.join(i).strip() for i in td]
        result.append(dict(zip(title, row)))
    return result


if __name__ == '__main__':
    target = '110.75.129.5'
    print(execute(target))
