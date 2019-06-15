# coding:utf-8
'''
filename: goods.py
'''
class Goods:
    def __init__(self, sales_number, price, discount_number=5):
        self.sales_number = sales_number
        self.price = price
        self.discount_number = discount_number
        d = self.sales_number - self.discount_number
        if d >= 0:
            if d <= 11:
                self.discount_percent = 0.9
            else:
                self.discount_percent = 0.8
        else:
            self.discount_percent = 0.99

    def sale_number(self):
        return self.sales_number

    def total(self):
        t = self.sales_number * self.price * self.discount_percent
        return t

apple = Goods(10, 9)
print("number: ", apple.sale_number())
print("total: ", apple.total())