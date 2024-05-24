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
  -t {icp,ipv6,company_name,host:port,ipv4,url,ip,domain}
                        指定输入类型（必须）
  -d {whois,域名历史解析,资产测绘,ip信誉,HTTP源代码,网站权重,端口检测,ip反查域名,icp备案,HTTP状态,归属地,子域名,ping检测}
                        指定插件功能（可选）
  -n {dnsgrep,webscan,icp.chinaz-1,baidu,ip138-1,ti.sangfor,rapiddns,whois.chinaz,pearktrue.cn-1,fofa-2,tool.chinaz-3,aizhan,ping.chinaz,beianx,tool.chinaz-1,chaziyu,dnslytics,fofa-4,pywhois,tool.chinaz-2,oioweb-1,pearktrue.cn-2,oioweb-2,alexa.cn,threatbook,aa1.cn-1,ip138-2,ip.tool.chinaz,shodan,fofa-3,fofa-1,yougetsignal,dns.aizhan}
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
| ping.chinaz | domain,ipv4 | ping检测 |
| pywhois | domain | whois |
| rapiddns | ipv4 | ip反查域名 |
| shodan | ipv4 | 资产测绘 |
| threatbook | ipv4 | ip信誉 |
| ti.sangfor | ipv4 | ip信誉 |
| tool.chinaz-1 | host:port | 端口检测 |
| tool.chinaz-2 | domain,url | HTTP状态 |
| tool.chinaz-3 | domain,url | HTTP源代码 |
| webscan | ipv4 | ip反查域名 |
| whois.chinaz | domain | whois |
| yougetsignal | ipv4 | ip反查域名 |