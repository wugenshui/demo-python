# 打印文本

print("this is a line with \n")
print(r"this is a line with \n")

# 单行注释

'''
多行注释
第二行注释
'''

# 条件判断
if False:
    print("if")
elif True:
    print("elif")
else:
    print("else")

# 输入文本
# inStr = input("\n\n按下 enter 键后退出。")
# print(inStr)

# 函数 打印斐波那契数列
def fib(n):
    a, b = 0, 1
    while a < n:
      print(a, end=' ')
      a, b = b, a+b
    # print()
fib(1000)
