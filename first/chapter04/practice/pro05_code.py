# coding:utf-8
'''
编写程序，寻找能够被17整除的三位的正整数。
'''

lst = [n for n in range(100, 1000) if n % 17 == 0]
print(lst)