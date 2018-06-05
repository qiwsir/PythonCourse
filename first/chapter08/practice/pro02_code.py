#coding:utf-8
'''
2. 有一个文件，其内容为每行一个数字，但是，有的行可能是别的内容，如空行或者注释等。样式如下：

```
#以下每行一个数字，但是有空行
1

2
5

9

```

请编写程序，将所有数字取出。
'''

def raises(err, func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except err:
        return True
    else:
        return False

numbers = [float(line) for line in open('pro02_txt.txt') if not raises(ValueError, float, line)]
print(numbers)

#也可以使用下面的函数
def returns(err, func, *args, **kwargs):
    try:
        return [func(*args, **kwargs)]
    except err:
        return []

numbers2 = [x for line in open('pro02_txt.txt') for x in returns(ValueError, float, line)]
print(numbers)