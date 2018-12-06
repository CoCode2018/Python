# 使用while循环输入1-10
count = 0
while count < 10:
    count += 1
    # if count == 7:
    #     print(' ')
    # else:
    #     print(count)
    if count == 7:
        continue
    print(count)

# 输出1-100内的所有奇数
count = 1
while count <= 100:
    if count % 2:
        print(count)
    count += 1

# 输出1-100内的所有偶数
# 每次都要执行的语句，比如循环增量；必须放在continue之前
count = 0
while count < 100:
    count += 1
    if count % 2:
        continue
    print(count)

# 求1-2+3-5....+99的和
sum = 0
count = 1
while count < 100:
    if count % 2:
        sum += count
    else:
        sum -= count
    count += 1
print(sum)

# 登录三次
NAME = 'ZhouGua'
PASSWD = '000000'
count = 1
while True:
    name = input("Enter your name: ")
    passwd = input("Enter yout password: ")
    if name == NAME and passwd == PASSWD:
        print('登录成功')
        break
    else:
        print('输入用户名或密码错误')
    if count == 3:
        print('尝试次数太多，请稍后再试')
        break
    count += 1

# 登录三次2
NAME = 'ZhouGua'
PASSWD = '000000'
count = 0
while count < 3:
    name = input("Enter your name: ")
    passwd = input("Enter yout password: ")
    if name == NAME and passwd == PASSWD:
        print('登录成功')
        break
    else:
        print('输入用户名或密码错误,请重试！')
    count += 1
else:
    print('尝试次数太多，请稍后再试')