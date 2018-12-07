# 列表

list1 = [1, 2, 3, 4,]

# ========================改
# 列表尾部追加一个元素
list1.append()

while 1:
    ele = input("Enter a element: ")
    if ele == 'q':
        break
    else:
        list1.append(ele)
    
# 给定索引位置,按照位置添加
list1.insert(0, 0)
# 迭代追加(iterable)
# 把可迭代的参数拆分, 然后追加到尾部
list1.extend([99, 100, 101])


# ========================删
# pop(), 按索引位置删除元素，默认为最后一个元素
list1.pop(len(list1)-1)
list1.pop(0)

# remove()
list1.remove(100)

# clear()
list1.clear()

# del
del list1


# ========================改
list1 = [1, 2, 3, 4]
list1[0] = 0
# list1[:3] = 1
list1[:3] = [1]
list1[:3] = '1'
list1[:3] = '1234567'
# ========================查