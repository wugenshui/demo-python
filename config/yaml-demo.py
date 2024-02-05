import yaml
 
# 读取配置文件
with open('config/config.yaml', 'r') as configfile:
    config = yaml.safe_load(configfile)
 
# 获取配置项的值
value = config['section']['option']
 
# 更新配置项的值
config['section']['option'] = 'new_value'
 
# 写入到配置文件
with open('config/config.yaml', 'w') as configfile:
    yaml.safe_dump(config, configfile)
