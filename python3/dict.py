dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com', 'people': { 'name': '张三' }}
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

del tinydict['name'] # 删除键 'Name'
tinydict.clear()     # 清空字典
del tinydict         # 删除字典