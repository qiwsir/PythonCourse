#coding:utf-8

'''
第一问：
>>> lst = [2, 4, -7, 19, -2, -1, 45]
>>> [n for n in lst if n < 0]
[-7, -2, -1]

第二问：
>>> marks = {'python': 89, 'java': 58, 'physics': 65, 'math': 87, 'chinese': 74, 'english': 60}
>>> average = sum(marks.values()) / len(marks)
>>> average
72.16666666666667
>>> {k: v for k,v in marks.items() if v >= average}
{'python': 89, 'math': 87, 'chinese': 74}

第三问：
>>> sum(x * x for x in range(1, 101))
338350
'''