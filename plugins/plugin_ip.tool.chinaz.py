import os
import execjs
import requests

requests.packages.urllib3.disable_warnings()

def info():
    _info = {
        'name': 'ip.tool.chinaz',
        'type': ['ipv4'],
        'desc': '归属地'
    }
    return _info

def execute(target):
    headers = {
        'Host': 'ip.tool.chinaz.com',
        # 'Content-Length': '36',
        'Sec-Ch-Ua': '"Not A(Brand";v="24", "Chromium";v="110"',
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://ip.tool.chinaz.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ip.tool.chinaz.com/siteip',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close',
    }

    params = {
        'at': 'ip',
        'callback': '',
    }
    js_path = None
    for file in ['./generatetoken.js','./plugins/generatetoken.js']:
        if os.path.exists(file):
            js_path = file
            break
    ctx = execjs.compile(open(js_path, 'r', encoding='utf8').read())
    data = {
        'ip': target,
        'token': ctx.call('generateHostKey', target),
    }

    r = requests.post('https://ip.tool.chinaz.com/ajaxsync.aspx',
                      params=params, headers=headers, data=data, verify=False)
    r.encoding = r.apparent_encoding
    return execjs.eval(r.text)


if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
