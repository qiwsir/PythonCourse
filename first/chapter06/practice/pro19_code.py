#coding:utf-8

class LowerStr(str):
    def __init__(self, *args):
        self._lowered = str.lower(self)
    def __repr__(self):
        return self._lowered
    __str__ = __repr__
    def __hash__(self):
        return hash(self._lowered)

a = LowerStr('AAA.aa')
print(a.split('.'))
print(dir(a))