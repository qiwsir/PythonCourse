#coding:utf-8

class Book:
    prices = {'Learn Python with Laoqi':45.7, 'Physics':56.7, 'Math':67.8}    # 书及其价格
    shipping = 5    # 快递费
    def __init__(self, name, num, free_ship):
        self.name = name
        self.num = num
        self.free_ship = free_ship   # 阈值
    def totals(self):
        price = Book.prices.get(self.name)
        if price:
            total = price * self.num
            return (total+Book.shipping) if total < self.free_ship else total
        return 'There is not book {0}'.format(self.name)

py = Book('Learn Python with Laoqi', 2, 88)
py_total = py.totals()
print("I bought {num} books {name}, The price is {price}￥".format(num=py.num, name=py.name, price=py_total))