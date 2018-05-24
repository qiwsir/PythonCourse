#coding:utf-8
'''
    sys.exit() exit from the program.
    filename: exitprogram.py
'''

import sys

n = 10

while n > 0:
    n -= 1
    if n == 5:
        sys.exit()
    else:
        print(n)