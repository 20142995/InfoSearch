import argparse
import importlib
import os
import traceback
import sys
import xlsxwriter
from prettytable import PrettyTable
sys.dont_write_bytecode = True


def list2xlsx(excle_name, **tables):
    workbook = xlsxwriter.Workbook(excle_name)
    for name, rows in tables.items():
        if not rows:
            continue
        worksheet = workbook.add_worksheet(name)
        for index, row in enumerate(rows):
            worksheet.write_row(index, 0, row)
    workbook.close()


# 加载插件
plugin_dir = 'plugins'  # 插件目录
plugins = []
for file in os.listdir(plugin_dir):
    if file == '__init__.py' or not file.endswith('.py'):
        continue
    _file = os.path.join(plugin_dir, file)
    try:
        _spec = importlib.util.spec_from_file_location(_file, _file)
        _module = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(_module)
        if hasattr(_module, 'execute') and hasattr(_module, 'info'):
            plugins.append(_module)
    except Exception as e:
        traceback.print_exc()

# 生成选项
type_choices = []
desc_choices = []
name_choices = []
for plugin in plugins:
    type_choices += plugin.info()['type']
    desc_choices += plugin.info()['desc']
    name_choices.append(plugin.info()['name'])
    # print(plugin.info()['name'],plugin.info()['type'],plugin.info()['desc'])



# 定义命令行参数
parser = argparse.ArgumentParser(description='批量查询')
parser.add_argument('-i', dest='target', help='目标')
parser.add_argument('-t', dest='type', choices=set(type_choices), help='过滤 类型')
parser.add_argument('-d', dest='desc', choices=set(desc_choices), help='过滤 功能')
parser.add_argument('-n', dest='name', choices=set(name_choices), help='过滤 名称')
parser.add_argument('-o', dest='outfile', help='保存结果eg: “results.xlsx”')

# 解析命令行参数
args = parser.parse_args()
# args.target = 'qq.com'
# args.type = 'domain'
if not args.target:
    parser.print_help()
else:
    targets = []
    if os.path.isfile(args.target):
        targets = [_.strip()
                   for _ in open(args.target, 'r', encoding='utf8').readlines()]
    else:
        targets = [args.target,]

    # 按设置过滤插件
    filtered_plugins = []
    if args.type:
        filtered_plugins = [plugin for plugin in plugins if args.type in plugin.info()[
            'type']]
    else:
        filtered_plugins = plugins

    if args.desc:
        filtered_plugins = [
            plugin for plugin in filtered_plugins if args.desc in plugin.info()['desc']]

    if args.name:
        filtered_plugins = [plugin for plugin in filtered_plugins if args.name in plugin.info()[
            'name'].lower()]
    results = {}
    for plugin in filtered_plugins:
        name = plugin.info()['name']
        desc = plugin.info()['desc']
        result = []
        for target in targets:
            try:
                for item in plugin.execute(target):
                    _ = {'*名称*': name, '*功能*': desc, '*目标*': target}
                    _.update(item)
                    result.append(_)
            except Exception as e:
                print(f'{name} {desc} {target} {e}')
        if result:
            results.setdefault(name, [])
            title = list(result[0].keys())
            results[name].append(title)
            table = PrettyTable(title)
            for item in result:
                row = [str(item.get(t, '')) for t in title]
                table.add_row(row)
                results[name].append(row)
            print(table)

    if args.outfile:
        list2xlsx(args.outfile, **results)
