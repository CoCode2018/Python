# 格式化输出
name = input("Enter you name: ")
age = int(input("Enter your age: "))
height = float(input('Enter your tall: '))
print("So, your name is %s, age is %d and tall is %.2f" % (name, age, height))

msg1 = """---------- info of %s ----------
Name    ：  %s
age     ：  %d
height  ：  %.2f
---------- end ----------""" %(name, name, age, height)
print(msg1)

msg2 = f"""---------- info of {name} ----------
Name    ：  {name}
age     ：  {age}
height  ：  {height}
---------- end ----------"""
print(msg2)