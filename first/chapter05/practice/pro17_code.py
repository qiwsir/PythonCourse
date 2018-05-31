#coding:utf-8
'''
17. 在字典类型对象中，有get方法，但是，在列表中，没有类似方法。比如，完成如下操作，就只能报错了。

```
    >>> lst = ["a", "b"]
    >>> lst[3]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range
```

所以，要解决这个问题。请编写一个函数，对列表实现类似字典中get方法。

'''
#method 1
def get_by_index(lst, i, value=None):
    if i < len(lst):
        return lst[i]
    else:
        return value

#method 2
def get_by_index(lst, i, value=None):
    if -len(lst) <= i < len(lst):
        return lst[i]
    else:
        return value

#method 3
def get_by_index(lst, i, value=None):
    try:
        return lst[i]
    except IndexError:
        return value
