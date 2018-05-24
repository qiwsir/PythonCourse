#coding:utf-8
'''
    define a new object type.
    filename: roundfloat.py
'''

class RoundFloat:
    def __init__(self, val):
        self.value = round(val, 2)
    
    def __str__(self):
        return "{0:.2f}".format(self.value)

    __repr__ = __str__

r = RoundFloat(3.1)
print(r)
print(type(r))