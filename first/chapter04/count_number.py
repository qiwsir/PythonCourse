#coding:utf-8
'''
   the times of each number appearing in tuple.
   filename: count_number.py 
'''
t = (3, 6, 1, 0, 2, 4, 6, 0, 8, 10, 7, 4, 0, 2, 0, 10, 6, 2, 4, 1)
d = dict()
for n in t:
    if n in d:
        d[n] += 1
    else:
        d[n] = 1
print(d)