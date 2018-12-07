str1 = 'abcdefg higklmn'
print(str1)

# 索引
print(str1[2])

# 切片,顾头不顾尾
print(str1[:4])
# 默认步长为1，方向从左到右，左侧数字代表的位置位于右侧数字代表的位置的左边(左侧数字更靠左)
print(str1[-5:-1])
# 设置步长，间隔 (步长-1) 个元素去一个值
print(str1[::3])
# 设置步长为负数时，方向从右往左，左侧数字代表的位置更靠右
print(str1[-1:-5:-1])
print(str1[(len(str1) - 1) : (len(str1) - 5) : -1])
print(str1[::-2])
# 复制序列
print(str1[:])
# 逆向复制
print(str1[::-1])

# 内置函数
len()
# 字符串方法

"""
str1.capitalize()
str1.upper()
str1.lower()
str1.swapcase()
str1.startswith()
str1.endswith()
str1.count()
str1.find()
str1.index()
str1.replace()
str1.isdigit()
str1.isalpha()

str1.split()
str1.lstrip()
str1.rsplit()
str1.center()
str1.format()
    按位置填写{}
    按索引填写{0}{2}{1}
    按变量名填写{name}

"""