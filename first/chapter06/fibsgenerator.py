#coding:utf-8
'''
    the generator of Fibonacci sequence.
    filename: fibsgenerator.py
'''

def fibs():
    prev, curr = 0, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr


import itertools
print(list(itertools.islice(fibs(), 10)))