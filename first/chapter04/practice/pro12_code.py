#coding:utf-8
'''
    12. 根据进制转化的原理，编写程序，实现十进制整数向二进制数的转化（请读者搜索并阅读有关“进制转化”的原理知识）。
    filename: pro12_code.py
'''

dec_num = 123
bin_lst = []
while True:
    quotient, remainder = divmod(dec_num, 2)
    bin_lst.append(str(remainder))
    if quotient == 0:
        break
    else:
        dec_num = quotient

bin_result = "".join(bin_lst[::-1])

bin_by_bin = bin(123)

print("the result by custom method:", bin_result)
print("the result by built-in method:", bin_by_bin)