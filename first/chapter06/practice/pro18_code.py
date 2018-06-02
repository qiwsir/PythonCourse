#coding:utf-8
'''
18. 替换字符串中的某些某部分，比如“This is a book”字符串，将其中的“a”替换为“one”。
参考：https://songlee24.github.io/2014/09/01/python-library-02/
https://docs.python.org/3/library/re.html
'''

import re

#method 1
def multiple_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)

#method 2
class make_xlat:
    def __init__(self, *args, **kwargs):
        self.adict = dict(*args, **kwargs)
        self.rx = self.make_rx()
    def make_rx(self):
        return re.compile('|'.join(map(re.escape, adict)))
    def one_xlat(self, match):
        return self.adict[match.group(0)]
    def __call__(self, text):
        return self.rx.sub(self.one_xlat, text)

if __name__ == "__main__":
    text = "It is a good person."
    adict = {"a good": "ONE", 'person':"human"}
    rp = make_xlat(adict)
    r = rp(text)
    print(r)
    # r = multiple_replace(text, adict)
    # print(text)
    # print(r)