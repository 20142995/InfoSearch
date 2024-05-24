import argparse
import importlib
import os
import traceback
import sys
import xlsxwriter
from prettytable import PrettyTable

sys.dont_write_bytecode = True


def export_to_excel(excel_name, **tables):
    workbook = xlsxwriter.Workbook(excel_name)
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
    plugin_file = os.path.join(plugin_dir, file)
    try:
        plugin_spec = importlib.util.spec_from_file_location(plugin_file, plugin_file)
        plugin_module = importlib.util.module_from_spec(plugin_spec)
        plugin_spec.loader.exec_module(plugin_module)
        if hasattr(plugin_module, 'execute') and hasattr(plugin_module, 'info'):
            plugins.append(plugin_module)
    except Exception as e:
        traceback.print_exc()

# 生成选项
type_choices = []
desc_choices = []
name_choices = []
for plugin in plugins:
    type_choices += plugin.info()['type']
    desc_choices.append(plugin.info()['desc'])
    name_choices.append(plugin.info()['name'])
    # print(f"| {plugin.info()['name']} | {','.join(plugin.info()['type'])} | {plugin.info()['desc']} |")


# 定义命令行参数
parser = argparse.ArgumentParser(description='批量查询')
parser.add_argument('-i', dest='target', help='目标（必须）')
parser.add_argument('-t', dest='type', choices=set(type_choices), help='指定输入类型（必须）')
parser.add_argument('-d', dest='desc', choices=set(desc_choices), help='指定插件功能（可选）')
parser.add_argument('-n', dest='name', choices=set(name_choices), help='指定插件名称（可选）')
parser.add_argument('-o', dest='outfile', help='保存结果eg: “results.xlsx” （可选）')

# 解析命令行参数
args = parser.parse_args()

if not args.target or not args.type:
    parser.print_help()
else:
    targets = []
    if os.path.isfile(args.target):
        targets = [_.strip() for _ in open(args.target, 'r', encoding='utf8').readlines()]
    else:
        targets = [args.target,]

    # 按设置过滤插件
    filtered_plugins = []
    if args.type:
        filtered_plugins = [plugin for plugin in plugins if args.type in plugin.info()['type']]
    else:
        filtered_plugins = plugins

    if args.desc:
        filtered_plugins = [plugin for plugin in filtered_plugins if args.desc in plugin.info()['desc'].lower()]

    if args.name:
        filtered_plugins = [plugin for plugin in filtered_plugins if args.name in plugin.info()['name'].lower()]

    results = {}
    for plugin in filtered_plugins:
        plugin_name = plugin.info()['name']
        plugin_desc = plugin.info()['desc']
        result = []
        for target in targets:
            try:
                items = plugin.execute(target)
                print(f'[{plugin_name}] -< {target} -> {len(items)}')
                for item in items:
                    row_data = {'*名称*': plugin_name, '*功能*': plugin_desc, '*目标*': target}
                    row_data.update(item)
                    result.append(row_data)
            except Exception as e:
                print(f'[{plugin_name}] -< {target} -> {e}')
        if result:
            results.setdefault(plugin_name, [])
            title = list(result[0].keys())
            results[plugin_name].append(title)
            table = PrettyTable(title)
            for item in result:
                row = [str(item.get(t, '')) for t in title]
                table.add_row(row)
                results[plugin_name].append(row)
            print(table)

    if args.outfile:
        export_to_excel(args.outfile, **results)
