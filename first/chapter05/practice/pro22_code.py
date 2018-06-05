#coding:utf-8
'''
22. 假设列表中有多个文件名，['a.py', 'b.jpg', 'c.gif', 'd.map', 'e.png', 'f.jpg', 'k.txt', 'f.gif', 'h.png', 'm.docx']，编写程序，从这些文件中选出图片文件，即扩展名分别是('.jpg', '.gif', '.png')的文件。
'''

def any_true(predicate, sequence):
    return True in map(predicate, sequence)

list_dir = ['a.py', 'b.jpg', 'c.gif', 'd.map', 'e.png', 'f.jpg', 'k.txt', 'f.gif', 'h.png', 'm.docx']
for filename in list_dir:
    if any_true(filename.endswith, ('.jpg', '.gif', '.png')):
        print(filename)