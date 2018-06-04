'''
4. heapq模块是Python标准库的一员，它实现了“堆”队列的各种算法，官方文档是：https://docs.python.org/3/library/heapq.html，请认真阅读文档，并结合其它有关资料，学习heapq模块中各种函数的使用方法。然后解决如下问题：

    - 从列表[38, 45, 19, 9, -12, 3, 97, 79, 199, 20, -49]中分别获得最大和最小的3个元素；
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
第一问：
>>> import heapq
>>> n = [38, 45, 19, 9, -12, 3, 97, 79, 199, 20, -49]
>>> heapq.nlargest(3, n)
[199, 97, 79]
>>> heapq.nsmallest(3, n)
[-49, -12, 3]
第二问：
>>> lst1 = [1, 3, 5, 7, 9]
>>> lst2 = [2, 4, 6, 8]
>>> import heapq
>>> r = heapq.merge(lst1, lst2)
>>> list(r)
[1, 2, 3, 4, 5, 6, 7, 8, 9]

第三问：
>>> books_price = [{"book": "python", "price": 69.99}, {"book": "java", "price": 59.99}, {"book": "rust", "price": 79.99}, {"book": "javascript", "price": 49.99}, {"book": "c++", "price": 89.99}, {"book": "ruby", "price": 39.99}, {"book": "hadoop", "price": 99.99}, {"book": "html5", "price": 29.99},]
>>> cheap = heapq.nsmallest(2, books_price, key=lambda x: x['price'])
>>> cheap
[{'book': 'html5', 'price': 29.99}, {'book': 'ruby', 'price': 39.99}]
>>> expensive = heapq.nlargest(2, books_price, key=lambda x: x['price'])
>>> expensive
[{'book': 'hadoop', 'price': 99.99}, {'book': 'c++', 'price': 89.99}]

'''