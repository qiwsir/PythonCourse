# coding:utf-8
'''
在密码学中，恺撒密码（英语：Caesar cipher），是一种最简单且最广为人知的加密技术。它是一种替换加密的技术，明文中的所有字母都在字母表上向后（或向前）按照一个固定数目进行偏移后被替换成密文。例如，当偏移量是3的时候，所有的字母A将被替换成D，B变成E，以此类推。这个加密方法是以罗马共和时期恺撒的名字命名的，当年恺撒曾用此方法与其将军们进行联系。根据这些知识，请编写一段程序，实现用户输入加密的字符串和偏移量，之后显示加密后的密文（提示，可以使用zip()）
'''
s = input("Please input an English word: ")

while True:
    d = input("Please input offset: ")
    if d.isdigit():
        d = int(d)
        break
    else:
        print('you should input an int for offset.')

new_lst = []
for c in s:
    n = ord(c) + d
    if n <= 122:
        new_c = chr(n)
    else:
        delt = d - (n - 122)
        new_c = chr(delt + 65)     # chr(65) ==> A
    new_lst.append(new_c)

new_word = "".join(new_lst)
print(s, " ==> ", new_word)



