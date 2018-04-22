#coding:utf-8
'''
    Add to Force, F1 + F2
    filename: force.py
'''
import math

f1 = 20
f2 = 10
alpha = math.pi / 3

x_force = f1 + f2 * math.sin(alpha)
y_force = f2 * math.cos(alpha)

force = math.sqrt(x_force * x_force + y_force * y_force)

print("The result is: ", round(force, 2), "N")