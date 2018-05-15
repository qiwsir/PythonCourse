#coding:utf-8
'''
    classify number set.
    filename: classifynum.py
'''

class OddEven:
    def __init__(self, numbers):
        self.odds = [i for i in numbers if self.is_odd(i)]
        self.evens = [i for i in numbers if i not in self.odds]

    @staticmethod
    def is_odd(x):
        if x % 2 == 1:
            return True
        return False

n = [1, 5, 7, 9, 2, 4, 10, 3]
r = OddEven(n)
print(r.odds)
print(r.evens)