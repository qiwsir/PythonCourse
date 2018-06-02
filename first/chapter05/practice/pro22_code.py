#coding:utf-8

def any_true(predicate, sequence):
    return True in map(predicate, sequence)

list_dir = ['a.py', 'b.jpg', 'c.gif', 'd.map', 'e.png', 'f.jpg', 'k.txt', 'f.gif', 'h.png', 'm.docx']
for filename in list_dir:
    if any_true(filename.endswith, ('.jpg', '.gif', '.png')):
        print(filename)