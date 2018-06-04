#coding:utf-8
'''
20. 在内置对象类型中，列表、字典、元组等，都是“容器”，在标准库的collections模块中，有Sequence类，它能支持容器的常用操作。请使用collections.Sequence类，定义一种新的容器，要求容器中的对象必须按照一定顺序排列。
'''
import collections
import bisect

class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)


items = SortedItems([5, 1, 3])
print(list(items))
print(items[0], items[-1])
items.add(2)
print(list(items))