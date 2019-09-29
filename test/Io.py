f = open('G:/Users/yang/Desktop/Timers.txt', 'r', encoding='utf-8')

# print(f.read())

# f.close()

print("-----------------with  as  -------------------")
# 一次性读取全部文件内容
with open('G:/Users/yang/Desktop/Timers.txt', 'r', encoding='utf-8') as f:
    # print(f.read())
    for line in f.readline():
        print(line.strip())



print("-----------------stringIO-------------------")

from io import StringIO

f = StringIO()
f.write('hello\nworld ')
f.write('hello world ')


print(f.getvalue())

print("-----------------os IO-------------------")

import os
print(os.name)
# windows 操作系统上没有
#print(os.uname())