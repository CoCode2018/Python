# 1
name = 'aleX leNb'
print(name.strip())
print(name[2:])
print(name[:-2])
print(name[1:-1])
print(name.startswith('al'))
print(name.endswith('Nb'))
print(name.replace('l', 'p'))
print(name.replace('l', 'p', 1))
print(name.split('l'))
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.count('l', 0, 4))
print(name.index('N'))
print(name.find('N'))
print(name.find('Xle'))

# 2
S = '132a4b5c'

# 3
s = 'asdfer'
for x in s:
    print(x)
index = 0
while index < len(s):
    print(s[index])
    index += 1

# 4
sum = 0
content = input('请输入内容(x + y)：')
content_li = content.split('+')

# int('1 ') == int('1')
# x = int(content_li[0].strip())
# y = int(content_li[1].strip())
# sum = x + y 
# print(sum)

for x in content_li:
    sum += int(x)
print(sum)
# 5
conut = 0
content = input("Enter the content: ")
for x in content:
    if x.isdigit():
        conut += 1
print(conut)

# 6
conut = 0
li = []
content = input("Enter the content: ")
while conut < len(content):
    if content[conut].isdigit():
        li.append(conut)

for x in content:
    if x.isdigit():
        print(x.index())
print(conut)