#coding:utf-8
'''
    convert upper and lower in a string.
    filename: convertupperlower.py
'''

def convert(s):
    lst = [i.upper() if i==i.lower() else i.lower() for i in s]
    return ''.join(lst)

s = "Hello, World"
c = convert(s)
print(c)