#coding:utf-8
'''
23. 有列表[1, "a", 2, "b", 3, "c", 4, "d"]，要求交替使用列表中的元素作为字典的键和值，创建一个字典，即得到字典{1: "a", 2: "b", 3: "c", 4: "d"}。
'''

def dct_from_seq(seq):
    return dict(zip(seq[::2], seq[1::2]))

lst = [1, "a", 2, "b", 3, "c", 4, "d"]
dct = dct_from_seq(lst)
print(dct)


#以下是另外一种实现方法，使用生成器函数
def pair_yield(seq):
    item_next = iter(seq).__next__
    while True:
        yield (item_next(),item_next())

def dct_from_yield(seq):
    return dict(pair_yield(seq))

dct2 = dct_from_yield(lst)
print(dct2)
