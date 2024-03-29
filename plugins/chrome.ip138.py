from DrissionPage import ChromiumOptions, ChromiumPage
import time


def info():
    _info = {
        'name': 'ip138',
        'type': ['ipv4',],
        'desc': ['IP反查域名']
    }
    return _info


def execute(target,debug=False):
    co = ChromiumOptions()
    if not debug:
        co.headless()
    page = ChromiumPage(co)
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
    print(execute(target,debug=True))
