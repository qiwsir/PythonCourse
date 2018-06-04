# 练习和编程

1. 有这样一个问题：一个列表，比如是[1, 2, 3]，在最右边增加一个数字。显然使用列表的append方法追加元素。

```
    >>> lst = [1, 2, 3]
    >>> lst.append(4)
    >>> lst
    [1, 2, 3, 4]
```

再进一步，能不能在最左边增加一个数字呢？比如在列表的左边增加整数7，或许下面的是一种方法：

```
    >>> nl = [7]
    >>> nl.extend(lst)
    >>> nl
    [7, 1, 2, 3, 4]
```

除了这种方法之外，Python标准库collections中提供了一个名为deque的模块。

```
>>> from collections import deque
```

请根据已经学习过的知识技能，研究deque（翻译为“双端队列”）的使用方法。

然后使用deque，解决下属问题：

自定义一个固定尺寸的缓存对象，当它被填满的时候，新加入一个元素后，第一元素，也就是最老的那个元素要被删除。

2. ScriPy是一个非常好的用于做“爬虫”的第三方包，请访问其官方网站，并在本地计算安装，然后自己选定网站，用ScriPy做爬虫，获取选定网站的有关内容。

3. datetime和calendar都是Python标准库中跟时间、日期相关的模块。请使用它们，计算上一个周五的日期，并以特定格式在控制台打印出来。

4. heapq模块是Python标准库的一员，它实现了“堆”队列的各种算法，官方文档是：https://docs.python.org/3/library/heapq.html，请认真阅读文档，并结合其它有关资料，学习heapq模块中各种函数的使用方法。然后解决如下问题：

    - 从列表[38, 45, 19, 9, -12, 3, 97, 79, 199, 20, -49]中分别获得最大和最小的3个元素；
    - 将两个已经排好序的列表[1, 3, 5, 7, 9]和[2, 4, 6, 8]合并，要求：合并后的对象也是按照从小到大排序的；
    - 以下表示的一些书的价格，请找出单价最高和最低的两本书。

```
    books_price = [
        {"book": "python", "price": 69.99},
        {"book": "java", "price": 59.99},
        {"book": "rust", "price": 79.99},
        {"book": "javascript", "price": 49.99},
        {"book": "c++", "price": 89.99},
        {"book": "ruby", "price": 39.99},
        {"book": "hadoop", "price": 99.99},
        {"book": "html5", "price": 29.99},
        ]
```

5. 对第三章35题中的字符串，统计出现频率最高的3个单词。

6. 第三章24题，曾经比较了列表的方法sort和内置函数sorted，对于内置函数sorted中的参数key，可以传入一个回调函数，此函数对每个传入的对象返回一个值，这个值会被函数sorted用作排序的关键词，更详细内容请参阅帮助文档。

    - 对第4题中的book_price按照“book”的值进行排序。（提示，可以使用operator模块中的itemgetter函数作为回调函数）
    - 有如下类型的对象：

```
    class User:
        def __init__(self, user_id):
            self.user_id = user_id
        def __repr__(self):
            return 'User({0})'.format(self.user_id)

    users = [User(2), User(11), User(3), User(9)]
```

对users按照user_id进行排序。