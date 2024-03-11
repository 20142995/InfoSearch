## 安装
```
pip install -r requirements.txt
```

## 使用帮助

```
usage: InfoSearch.py [-h] [-i TARGET] [-t {domain,ipv6,url,company_name,ipv4,icp}] [-d {IP反查域名,归属地,权重,ICP备案,资产测绘}] [-n {rapiddns,dnslytics,oioweb,yougetsignal,beianx,webscan,fofa,aizhan,chinaz,ip138,dnsgrep}] [-o OUTFILE]

批量查询

options:
  -h, --help            show this help message and exit
  -i TARGET             目标
  -t {domain,ipv6,url,company_name,ipv4,icp}
                        过滤 类型
  -d {IP反查域名,归属地,权重,ICP备案,资产测绘}
                        过滤 功能
  -n {rapiddns,dnslytics,oioweb,yougetsignal,beianx,webscan,fofa,aizhan,chinaz,ip138,dnsgrep}
                        过滤 名称
  -o OUTFILE            保存结果eg: “results.xlsx”
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