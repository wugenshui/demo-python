# 打开文件，遍历每一行
for line in open('test.txt','r',encoding='UTF-8'):
  # 清除行首行尾的换行符
  print(line.strip())

print('*' * 100)

# 打开文件，遍历每一行
file = open('test.txt','r',encoding='UTF-8')
# 清除行首行尾的换行符
print(file.read())
file.close()

