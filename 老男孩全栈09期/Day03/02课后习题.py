# 格式化字符串

w = '我'
n = '你'
t = '它'

str1 = '%s%s%s, 大家好!' % (w, n, t)
print(str1)
str2 = '{}{}{}, 大家好!'.format(w, n, t)
print(str2)
str3 = f'{w}{n}{t}, 大家好!'
print(str3)

# 1
print(1 > 1 or 3 < 4 or 4 < 5 and 2 > 1 and 9 > 8 or 7 < 6) # True
print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)    # False
print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8 and 4 > 6 or 3 < 2)   #False

# 2
print(8 or 3 and 4 or 2 and 0 or 9 and 7)   # 8
print(0 or 2 and 3 and 4 or 6 and 0 or 3) # 4
print(5 and 9 or 10 and 2 or 3 and 5 or 4 or 5) # 9

# 3
print(6 or 2 > 1)   # 6
print(3 or 2 > 1)   # 3
print(0 or 5 < 4)   # False
print(5 < 4 or 3)   # 3
print(2 > 1 or 6)   # True
print(3 and 2 > 1)  # True
print(0 and 3 > 1)  # 0
print(2 > 1 and 3)  # 3
print(3 > 1 and 0)  # 0
print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)    # 2

# 4
# 5
# 6
# 7
# 8
sum = 0
count = 0
while count < 100:
    count += 1
    if count == 88:
        continue
    if count % 2:
        sum += count
    else:
        sum -= count
print(sum) 
# 8-2
sum = 0
sign = -1
count = 0
while count < 100:
    count += 1
    sign = -sign
    if count == 88:
        continue
    else:
        sum += count * sign
print(sum)
# 9
count = 3
while count > 0:
    name = input("Enter your name: ")
    passwd = input("Enter your Password: ")

    if name == 'ZhouGua' and passwd == '000000':
        print("登录成功！")
        break
    else: 
        count -= 1
        print('剩余机会：%d次' % count)
else:
    print('尝试次数太多，稍后再试！')
# 13
name = input("Enter your name: ")
place = input("Enter your favourite place: ")
haby = input("Enter your haby: ")
print(f"敬爱可亲的{name}，最喜欢在{place}地方干{haby}")

# 14

while True:
    str1 = input("Enter your string: ")
    if '小粉嫩' in str1 or '大铁锤' in str1:
        print('您输入的是：%s' % str1)
        print('存在敏感字符请重新输入')
    else:
        print('您输入的是：%s' % str1)
        break