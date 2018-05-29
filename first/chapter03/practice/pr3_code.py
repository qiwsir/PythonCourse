#coding: utf-8
'''
3. 编写程序，分别计算圆的周长和面积，要求：

    - 提示用户输入圆的半径。
    - 用户输入半径之后，计算圆的周长和面积。
    - 将周长和面积的值打印出来，要求各自保留两位小数。

将上述程序保存到一个程序文件中（即“.py”文件），并执行此程序。
'''

import math

radius = float(input("Enter the radius of circle:"))
circumference = 2 * math.pi * radius
area = math.pi * radius * radius

print("The circumference is :", round(circumference, 2))
print("The area is :", round(area, 2))