
# 逻辑运算符
    # 1.True/False
    # 2.数字
    # 3.数字和True/False混合, 返回使得表达式返回的值, True/False/数字

# 优先级: () 》not 》and 》or

print(2 > 1 and 1 < 4 or 2 < 3 and 9 > 6 or 2 < 4 and 3 < 2)
# 先算and两边的操作数数
# T or T or F
# T or F
# T

# F or F = F
print(3 > 4 or 4 < 3 and 1 == 1)
# T
print(1 < 2 and 3 < 4 or 1 > 2)
# T or F = T
print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)
# F or F or F = F
print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)
# F or F and T or F = F
print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# F or F or F = F
print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)

# 数字和bool类型转换
# 非零数字为True
# 0为False
print(bool(1))
print(bool(-1))
print(bool(0))

# True 为 1
# False 为 0
print(int(True))
print(int(False))

# F or F = F
print(1 > 2 and 3 or 4 and 3 < 2)
print(1 > 2 and 3)
print(1 < 2 and 3 and 3 < 2)
print(1 > -1 and True)
