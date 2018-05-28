#coding:utf-8
'''
    add two numbers in a command line
    filename: commandadd.py
'''

import sys

lam = lambda x, y: x + y

x = float(sys.argv[1])
y = float(sys.argv[2])
print("x + y = ",lam(x, y))