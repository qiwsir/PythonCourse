#coding:utf-8
'''
17. 编写程序，输入一个5位数，判断它是不是回文数。例如“12321”是回文数。
'''

a = int(input("enter a integer:"))
x = str(a)
flag = True

for i in range(int(len(x)/2)):
    if x[i] != x[-i - 1]:
        flag = False
        break

if flag:
    print("{0} is palindromic number".format(a))
else:
    print("{0} is not palindromic number".format(a))