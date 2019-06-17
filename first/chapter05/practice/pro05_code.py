# coding:utf-8
"""
编写函数，能够返回两个自然数在某范围内的公倍数，比如计算3和10在100以内的公倍数。
"""
def common_multiple(a, b, nmin=0, nmax=1000):
    if nmin < nmax:
        return [i for i in range(nmin, nmax) if i % a == 0 and i % b == 0]
    else:
        print("nmin must less than nman.")
        return None

cm = common_multiple(3, 7)
print(cm)