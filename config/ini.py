import configparser
 
# 创建ConfigParser对象
config = configparser.ConfigParser()
 
# 读取配置文件
config.read('config/config.ini')
 
# 获取配置项的值
value = config.get('section', 'option')
 
# 更新配置项的值
config.set('section', 'option', 'new_value')
 
# 写入到配置文件
with open('config/config.ini', 'w') as configfile:
    config.write(configfile)