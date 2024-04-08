## 安装
```
pip install -r requirements.txt
```

## 使用帮助

```
usage: InfoSearch.py [-h] [-i 目标] [-t 输入参数类型] [-d 功能名称] [-n 插件名称] [-o 结果文件名称]

批量查询

options:
  -h, --help            show this help message and exit
  -i TARGET             目标（必须）
  -t {domain,icp,company_name,ip,ipv4,ipv6,url}
                        指定输入类型（必须）
  -d {域名历史解析,资产测绘,whois,ip信誉,网站权重,icp备案,ip反查域名,归属地,子域名}
                        指定插件功能（可选）
  -n {dnsgrep,ip.tool.chinaz,threatbook,fofa-3,aa1.cn-1,alexa.cn,shodan,beianx,icp.chinaz-1,webscan,ip138-2,pywhois,fofa-1,aizhan,yougetsignal,baidu,fofa-4,oioweb-1,pearktrue.cn-1,rapiddns,chaziyu,pearktrue.cn-2,dnslytics,dns.aizhan,fofa-2,oioweb-2,ip138-1,whois.chinaz}
                        指定插件名称（可选）
  -o OUTFILE            保存结果eg: “results.xlsx” （可选）
```

## 使用示例

### IP反查域名 (根据功能过滤)
```
python InfoSearch.py -t ipv4 -i 110.75.129.5 -d IP反查域名
```

### 查IP (根据输入类型过滤)
```
python InfoSearch.py -t ipv4 -i 110.75.129.5
```


### ip138 (根据插件名称过滤)
```
python InfoSearch.py -t ipv4 -i 110.75.129.5 -n ip138
```

## 当前支持
| 插件名称 | 输入类型 | 功能名称 |
| :--- | :--- | :--- |
| dnsgrep | ipv4 | ip反查域名 |
| dnslytics | ipv4 | ip反查域名 |
| aa1.cn-1 | domain,url | icp备案 |
| aizhan | domain | 网站权重 |
| alexa.cn | domain | icp备案 |
| baidu | ipv4 | 归属地 |
| beianx | domain,icp,company_name | icp备案 |
| chaziyu | domain | 子域名 |
| dns.aizhan | ipv4 | ip反查域名 |
| dnslytics | ipv4 | ip反查域名 |
| fofa-1 | ipv4 | 资产测绘 |
| fofa-2 | ipv4 | ip反查域名 |
| fofa-3 | domain | 资产测绘 |
| fofa-4 | ipv4,domain | 资产测绘 |
| icp.chinaz-1 | domain | icp备案 |
| icp.chinaz-1 | domain,icp,company_name | icp备案 |
| ip.tool.chinaz | ipv4 | 归属地 |
| ip138-1 | domain | 子域名 |
| ip138-2 | ip | ip反查域名 |
| ip138-2 | domain | 域名历史解析 |
| oioweb-1 | ipv4,ipv6 | 归属地 |
| oioweb-2 | domain | icp备案 |
| pearktrue.cn-1 | domain | 网站权重 |
| pearktrue.cn-2 | domain | icp备案 |
| pywhois | domain | whois |
| rapiddns | ipv4 | ip反查域名 |
| shodan | ipv4 | 资产测绘 |
| threatbook | ipv4 | ip信誉 |
| webscan | ipv4 | ip反查域名 |
| whois.chinaz | domain | whois |
| yougetsignal | ipv4 | ip反查域名 |