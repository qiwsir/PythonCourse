#coding:utf-8
'''
    Generates a sequence of parameters with floating-point numbers.
    filename: floatrange.py
'''

import itertools

def frange(start, end=None, step=1.0):
    if end is None:
        end = float(start)
        start = 0.0
    assert step
    for i in itertools.count():
        next = start + i * step
        if (step > 0.0 and next >= end) or (step < 0.0 and next <= end):
            break
        yield next


f = frange(1.2, 9)
print(list(f))