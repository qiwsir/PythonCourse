#coding:utf-8
'''
    moving window function
    filename: windowfunc.py
'''

import itertools

def spliter(iterable, n):
    result = [ [] for x in range(n)]   
    resiter = itertools.cycle(result)  
    for item, sublist in zip(iterable, resiter):
        sublist.append(item)
    return result

s = "abcde"
print(spliter(s, 3))
d = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
print(spliter(d, 3))