from DrissionPage import ChromiumOptions, ChromiumPage
import time


def info():
    _info = {
        'name': 'chinaz-4',
        'type': ['domain',],
        'desc': ['whois']
    }
    return _info


def execute(target,debug=False):
    co = ChromiumOptions()
    co.incognito()
    if not debug:
        co.headless()
    page = ChromiumPage(co)
    page.get('https://whois.chinaz.com/')
    page.ele('@id=DomainName').input(target)
    page.ele('@value=查询').click()
    time.sleep(3)
    lis = page.eles('xpath://div[@id="whois_info"]/li')
    result = []
    if lis:
        _info = {}
        for li in lis:
            row = [div.texts() for div in li.eles('t:div')]
            row = [i[0] for i in row if i]
            _info[';'.join(row[:1])] = ';'.join(row[1:])
        result.append(_info)
    return result


if __name__ == '__main__':
    target = 'qq.com'
    print(execute(target,debug=True))
