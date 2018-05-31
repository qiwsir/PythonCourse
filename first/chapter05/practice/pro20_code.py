#coding:utf-8
'''
20. 假设有若干个文件，文件名放到了列表中，然后对文件名进行排序。如下所示操作：

```
    >>> filenames = ["py1.py", "py2.py", "py10.py", "py14.py"]
    >>> filenames.sort()
    >>> filenames
    ['py1.py', 'py10.py', 'py14.py', 'py2.py']
```

显然上面的排序结果令人很不满意，按照通常的习惯，正确的排序结果应该是['py1.py', 'py2.py', 'py10.py', 'py14.py']。

请写一个函数，能够实现正确的排序结果。

'''

import re

def select_numbers(s):
    pieces = re.compile(r'(\d+)').split(s)    #convert string to str and number
    pieces[1::2] = map(int, pieces[1::2])     
    return pieces

def sort_filename(filename):
    return sorted(filename, key=select_numbers)

if __name__ == "__main__":
    files = ["py2.py", "py10.py", "py3.py"]
    result = sort_filename(files)
    print(files)
    print(result)