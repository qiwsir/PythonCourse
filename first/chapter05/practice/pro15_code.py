#coding:utf-8

"""
15. 编写一元二次函数，推荐应用5.2.2的“嵌套函数”知识。
y = ax^2 + bx + c
"""

def parabola(a, b, c):
    def para(x):
        return a * x * x + b * x + c
    return para

y = parabola(2, 3, 4)
r = y(3)
print("y = 2x^2 + 3x + 4 | x=3, the result = {0}".format(r))