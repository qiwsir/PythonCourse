#coding:utf-8

class Proverb:
    def __init__(self, name, word):
        self.name = name
        self.word = word
    def __repr__(self):
        return "{0.name}: {0.word}".format(self)

    __str__ = __repr__

ziyue = Proverb("子曰", "中午不睡，下午崩溃")
print(ziyue)