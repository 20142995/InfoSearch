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
  -t {url,ipv6,domain,company_name,ipv4,icp}
                        过滤 类型（必须）
  -d {IP反查域名,IP信誉,归属地,资产测绘,权重,ICP备案}
                        过滤 功能（可选）
  -n {chinaz-3,beianx,aizhan,webscan,fofa-3,oioweb-2,dnslytics,threatbook-1,yougetsignal,ip138,fofa-1,oioweb-1,chinaz-1,chinaz-2,dnsgrep,rapiddns,shodan-1,fofa-2}
                        过滤 插件名称（可选）
  -o OUTFILE            保存结果eg: “results.xlsx” （可选）
```

## 使用示例

### IP反查域名 (根据功能过滤)
```
python InfoSearch.py -d IP反查域名 -i 110.75.129.5
```

### 查IP (根据输入类型过滤)
```
python InfoSearch.py -t ip -i 110.75.129.5
```


### ip138 (根据插件名称过滤)
```
python InfoSearch.py -n ip138 -i 110.75.129.5
```

## 当前支持
| 插件名称 | 输入类型 | 功能名称 |
| :--- | :--- | :--- |
| oioweb-1 | ['ipv4', 'ipv6'] | ['归属地'] |
| oioweb-2 | ['domain'] | ['ICP备案'] |
| threatbook-1 | ['ipv4'] | ['IP信誉'] |
| webscan | ['ipv4'] | ['IP反查域名'] |
| fofa-1 | ['domain'] | ['资产测绘'] |
| fofa-2 | ['ipv4'] | ['IP反查域名'] |
| fofa-3 | ['ipv4'] | ['资产测绘'] |
| chinaz-1 | ['url', 'domain', 'icp', 'company_name'] | ['ICP备案'] |
| chinaz-2 | ['ipv4', 'domain'] | ['归属地'] |
| rapiddns | ['ipv4'] | ['IP反查域名'] |
| dnslytics | ['ipv4'] | ['IP反查域名'] |
| ip138 | ['ipv4'] | ['IP反查域名'] |
| chinaz-3 | ['ipv4'] | ['IP反查域名'] |
| aizhan | ['domain'] | ['权重'] |
| beianx | ['domain', 'icp', 'company_name'] | ['ICP备案'] |
| dnsgrep | ['ipv4'] | ['IP反查域名'] |
| shodan-1 | ['ipv4'] | ['资产测绘'] |
| yougetsignal | ['ipv4'] | ['IP反查域名'] |