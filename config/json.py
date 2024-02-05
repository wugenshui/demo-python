import json
 
# 读取配置文件
with open('config/config.json', 'r') as configfile:
    config = json.load(configfile)
 
# 获取配置项的值
value = config['section']['option']
 
# 更新配置项的值
config['section']['option'] = 'new_value'
 
# 写入到配置文件
with open('config/config.json', 'w') as configfile:
    json.dump(config, configfile)