#coding:utf-8
'''
    an iterator
    filename: iterator.py
'''

class MyRange:
    def __init__(self, n):
        self.i = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


print("rang(7):", list(range(7)))
print("MyRange(7):", [i for i in MyRange(7)])