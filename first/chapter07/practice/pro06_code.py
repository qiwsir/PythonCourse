#coding:utf-8

'''
第一问：
>>> books_price
[{'book': 'python', 'price': 69.99}, {'book': 'java', 'price': 59.99}, {'book': 'rust', 'price': 79.99}, {'book': 'javascript', 'price': 49.99}, {'book': 'c++', 'price': 89.99}, {'book': 'ruby', 'price': 39.99}, {'book': 'hadoop', 'price': 99.99}, {'book': 'html5', 'price': 29.99}]
>>> from operator import itemgetter
>>> by_book = sorted(books_price, key=itemgetter('book'))
>>> by_book
[{'book': 'c++', 'price': 89.99}, {'book': 'hadoop', 'price': 99.99}, {'book': 'html5', 'price': 29.99}, {'book': 'java', 'price': 59.99}, {'book': 'javascript', 'price': 49.99}, {'book': 'python', 'price': 69.99}, {'book': 'ruby', 'price': 39.99}, {'book': 'rust', 'price': 79.99}]
'''

#第二问：

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({0})'.format(self.user_id)

users = [User(2), User(11), User(3), User(9)]

from operator import attrgetter
result = sorted(users, key=attrgetter('user_id'))
lambda_result = sorted(users, key=lambda i: i.user_id)
print(result)
print(lambda_result)