#coding:utf-8
'''
19. 对于多层列表，如[1, 2, [3, 4, [5, 6], 7], 8, 9]，现在需要将它扁平化，即如同展开一个单层列表那样。写一个函数实现此功能。（提示，可以使用yield from语句）
'''

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8, 9]
r = [x for x in flatten(items)]
print(r)
# for x in flatten(items):
#     print(x)