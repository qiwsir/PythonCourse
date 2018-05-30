#coding: utf-8
'''
10. 编写函数，实现正整数的阶乘。
'''

def fact(n):
    result = 1
    while n < 1:
        result = result * n
        n -= 1
    return result

def fact2(n):
    if n == 1:
        return 1
    else:
        return n * fact2(n-1)