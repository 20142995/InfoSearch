from DrissionPage import ChromiumOptions, ChromiumPage
import time
import os


def info():
    _info = {
        'name': 'shodan-1',
        'type': ['ipv4',],
        'desc': ['资产测绘',]
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
    shodan_username = os.getenv('shodan_username')
    shodan_password = os.getenv('shodan_password')
    if shodan_username and shodan_password:
        page.get('https://account.shodan.io/login?continue=https%3A%2F%2Fwww.shodan.io%2Fdashboard')
        page.ele('@id=username').input(shodan_username)
        page.ele('@id=password').input(shodan_password)
        page.ele('@value=Login').click()
        time.sleep(2)
    
    page.get(f'https://www.shodan.io/host/{target}')
    time.sleep(2)
    result = []
    title = ['port','protocol']
    if page.eles('xpath://h6[@class="grid-heading" and @id]/span'):
        for port in page.eles('xpath://h6[@class="grid-heading" and @id]/span'):
            row = []
            port,protocol = port.texts()
            row.append(port)
            row.append(protocol.lstrip('/\n'))
            result.append(dict(zip(title, row)))
    else:
        result.append({'msg':'无结果，尝试设置环境变量shodan_username、shodan_password'})

    return result


if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
