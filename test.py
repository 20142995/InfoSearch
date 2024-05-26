
import importlib
import os
import traceback
import sys
from concurrent.futures import ThreadPoolExecutor

sys.dont_write_bytecode = True

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

test_data = {
    "ip":"8.8.8.8",
    "ipv4":"8.8.8.8",
    "ipv6":"2408:8719:2000:1c0:6c::12",
    "domain":"chinaz.com",
    "url":"https://www.chinaz.com/",
    "company_name":"厦门享联科技有限公司",
    "host:port":"8.8.8.8:53",


}
def run_task(arg):
    plugin,item = arg
    try:
        item['result'] = plugin.execute(item['target'])
    except:
        pass
    return item
test_result = []
tasks = []
# 插件测试
for plugin in plugins:
    for targe_type in plugin.info()['type']:
        try:
            item = {}
            item['name'] = plugin.info()['name']
            item['desc'] = plugin.info()['desc']
            item['targe_type'] = targe_type
            item['target'] = test_data.get(targe_type,'')
            item['result'] = []
            tasks.append((plugin,item))
        except:
            pass

t = ThreadPoolExecutor()
for r in t.map(run_task, tasks):
    print(r)