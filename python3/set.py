# 集合（set）是一个无序的不重复元素序列
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a 和 b 的差集

print(a | b)     # a 和 b 的并集

print(a & b)     # a 和 b 的交集

print(a ^ b)     # a 和 b 中不同时存在的元素

# 集合推导式(Set comprehension):
print({x for x in 'abracadabra' if x not in 'abc'})

# 添加单个元素
b.add('new')
print(b)

# update也可以添加元素，且参数可以是列表，元组，字典等
b.update({1,3})
print(b)

# 移除元素, 如果元素不存在，则会发生错误
b.remove('a')
print(b)

# 移除集合中的元素，且如果元素不存在，不会发生错误
b.discard('a')
print(b)

# 判断元素是否存在集合中
print('a' in b)

# 清空集合
b.clear()
print(b)