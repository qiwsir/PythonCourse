# coding:utf-8
'''
编写程序，判断用户输入的数字是偶数还是奇数。
'''
while True:
    n = input("Please input a int('q':exit this program): ")
    if n.isdigit():
        n = int(n)
        if n % 2 == 0:
            print("所输入的{}是偶数".format(n))
        else:
            print("所输入的{}是奇数".format(n))
        continue
    else:
        if n == 'q':
            break
        else:
            print("输入整数，请。")

