import whois


def info():
    _info = {
        'name': 'pywhois',
        'type': ['domain',],
        'desc': ['whois']
    }
    return _info

def get_whois(domain):
    results = []
    data = whois.whois(domain)
    title = ['输入','域名','注册商','联系人','联系邮箱','创建时间','过期时间']
    row = [domain,data.get('domain_name'),data.get('registrar'),data.get('name'),data.get('emails'),str(data.get('creation_date')),str(data.get('expiration_date'))]
    results.append(dict(zip(title,row)))
    return results

def execute(target):
    results = []
    data = whois.whois(target)
    title = ['域名','注册商','联系人','联系邮箱','创建时间','过期时间']
    row = [data.get('domain_name'),data.get('registrar'),data.get('name'),data.get('emails'),str(data.get('creation_date')),str(data.get('expiration_date'))]
    results.append(dict(zip(title,row)))
    return results


if __name__ == '__main__':
    target = 'qq.com'
    print(execute(target))
