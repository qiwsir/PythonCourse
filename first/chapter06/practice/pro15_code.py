#coding:utf-8

'''
15. 定义一个直角坐标系中的点类，并且以特殊方法__add__实现两个点坐标的相加。
'''

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(3, 4)
p2 = Point(8, 9)
p = p1 + p2
print(p)
