#coding:utf-8
'''
    understand continue in while loops.
    filename: whilecont.py
'''
a = 11

while a > 0:
    a -= 1
    if a % 2 == 0:
        continue
        print(a)
    else:
        print(a)
    