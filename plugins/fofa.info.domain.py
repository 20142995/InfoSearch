from DrissionPage import ChromiumOptions, ChromiumPage
import time
from urllib.parse import quote
import base64


def info():
    _info = {
        'name': 'fofa',
        'type': ['domain'],
        'desc': ['资产测绘']
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
    q = f'domain="{target}"'
    qbase64 = quote(base64.b64encode(q.encode('utf8')).decode())

    page.get(f'https://fofa.info/result?qbase64={qbase64}')
    page.ele('@class=iconfont icon-list-rich').click()
    time.sleep(2)
    div = page.ele('xpath://table[.//text()="序号"]/parent::div')
    th = [i.texts() for i in div.eles('xpath:table/thead/tr/th')]
    title = [i[0] for i in th if len(i) == 1]
    for tr in div.eles('xpath:following-sibling::div/table/tbody/tr'):
        td = [i.texts() for i in tr.eles('xpath:td')]
        row = [i[0] for i in td if len(i) == 1]
        result.append(dict(zip(title, row)))
    return result


if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
