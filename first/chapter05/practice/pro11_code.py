#coding:utf-8

def distance(pa, pb):
    import math
    lst = [(x-y)**2 for x, y in zip(pa, pb)]
    #lst = map(lambda x, y: (x-y)**2, pa, pb)
    d = math.sqrt(sum(lst))
    return d

pa = (1, 2)
pb = (3, 4)
print('d=', distance(pa, pb))