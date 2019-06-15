# coding:utf-8
'''
编写程序，求解一元二次方程2x^2 + 5x - 8 = 0，要求：将最终结果打印出来。
'''
import math

a = 1
b = 5
c = 8
delter = b * b - 4 * a * c
if delter > 0:
    sqrt_r = math.sqrt(delter)
    root1 = (-b + sqrt_r) / 2
    root2 = (-b - sqrt_r) / 2
    print("the root is: {0} and {1}".format(root1, root2))
elif delter == 0:
    root = - b / 2
    print("the root is: {}".format(root))
else:
    print('no root!')