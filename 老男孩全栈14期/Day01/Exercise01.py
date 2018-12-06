# -*- encoding: utf-8 -*-

# 输出
print("Hello World")

# 注释
    #  #号,单行注释
    #  三引号,多行注释

# 变量
print(1 + 3)
print((1 + 3) * 2)
print((1 + 3) * 2 - 6)
print(((1 + 3) * 2 - 6) * 3)

a = 1 + 3
print(a)

b = a * 2
print(b)

c = b - 6
print(c)

d = c * 3
print(d)

# 基本数据类型

# 数字类型
print(type(1))
print(type(1.1))
print(type(1 + 1j))
print(type(True))

print(5/2)
print(5//2)
print(5.0//2)
print(-5.0//2)
# 布尔类型
a = 1 > 2
print(a)
b = 2 > 1
print(b)

# 字符串类型
a = '呵呵'
b = "呵呵"
print(type(a))
print(type(b))

c = """我
你
他
"""
print(c)
print(type(c))

# 输出字符串
print('你好')
print('我好')
print('大家好')

print('你好' + '我好' + '大家好')
print('你好', '我好', '大家好')

print('你好', end=',')
print('我好', end='')
print('大家好', end='\n')

# 字符串拼接, +号两边只能是同类型对象
a = '1'
b = '2'
c = '3'
d = a + b + c
print(d)
# 字符串重复
d = '4 '
print(d * 4)
# 字符串索引
# 字符串分片
# 字符串迭代
# 字符串成员检测


# 用户交互
a = input("Enter a number: ")
b = input("Enter a number: ")
print(a + b)
print(type(a))
print(int(a) + int(b))

# if
gender = input('你是男的还是女的?')

if gender == '男':
    print('JJ')
print('GG')
