# coding:utf-8
'''
对于列表lst = [1, 2, 3, 4, 5]，将其中的偶数剔除，得到只有奇数的列表。
'''
lst = [1, 2, 3, 4, 5]
for i in lst:
    if i % 2 == 0:
        lst.remove(i)

print(lst)