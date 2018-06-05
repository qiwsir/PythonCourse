#coding:utf-8
'''
第一问：
>>> r = [ [row[i] for i in (0, 2, 3)] for row in lst ]
>>> for row in r:
...     print(row)
...
[1, 3, 4]
[5, 7, 8]
[9, 11, 12]

第二问：

方法1：
>>> new_lst = map(list, zip(*lst))
>>> for row in new_lst:
...     print(row)
...
[1, 5, 9]
[2, 6, 10]
[3, 7, 11]
[4, 8, 12]

方法2：
>>> for row in lst2:
...     print(row)
...
[1, 5, 9]
[2, 6, 10]
[3, 7, 11]
'''