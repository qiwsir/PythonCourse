#coding:utf-8
'''
编写一个程序，能够输出字符串“Hello”中每个“l”的索引值。将此程序保存到一个程序文件中（即“.py”文件），并执行此程序。
'''
s = "hello"
n = s.count("l")
index_lst = []
start = 0
for i in range(n):
    idx = s.index('l', start)
    start = idx + 1
    index_lst.append(idx)

print(index_lst)