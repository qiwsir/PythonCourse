#coding:utf-8
'''
    understand sys.argv
    filename: sysparemeter.py
'''

import sys

print("file name:", sys.argv[0])
print("length of argument", len(sys.argv))
print("arguments are: ", str(sys.argv))