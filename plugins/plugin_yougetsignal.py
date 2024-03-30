import requests

requests.packages.urllib3.disable_warnings()

def info():
    _info = {
        'name': 'yougetsignal',
        'type': ['ipv4',],
        'desc': 'ip反查域名'
    }
    return _info


def execute(target):

    url = "https://domains.yougetsignal.com/domains.php"
    headers = {"Sec-Ch-Ua": "\"Not A(Brand\";v=\"24\", \"Chromium\";v=\"110\"", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
               "X-Prototype-Version": "1.6.0", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://www.yougetsignal.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.yougetsignal.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9"}
    data = {"remoteAddress": target, "key": '', "_": ''}
    r = requests.post(url, headers=headers, data=data)
    rj = r.json()
    return [{'domain': i[0]} for i in rj.get('domainArray', [])]


if __name__ == '__main__':
    target = '8.8.8.8'
    print(execute(target))
