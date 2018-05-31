# coding:utf-8
'''
16. 对于字符串的显示，有时候要做一些处理，比如这样的字符串："Laoqi QQ group: 26913719"：

    - 如果把QQ群的序号看做“隐私”，则不予显示，或者显示为“*”；
    - 可以指定删除字符串中的某些字符，或者保留字符串中的某些字符。

'''
import string

def translator(frm='', to='', delete='', keep=None):
    if len(to) == 1:
        to = to * len(frm)
    
    if keep is not None:
        delete = "".join(set(string.printable).difference(keep)) if not delete else delete
    
    trans = str.maketrans(frm, to, delete)
    
    def translate(s):
        return s.translate(trans)

    return translate

if __name__ == "__main__":
    digits_only = translator(keep=string.digits)
    print(digits_only("Laoqi QQ group: 26913719"))
    no_digits = translator(delete=string.digits)
    print(no_digits("Laoqi QQ group: 26913719"))
    digits_to_hash = translator(frm=string.digits, to="*")
    print(digits_to_hash("Laoqi QQ group: 26913719"))
    trans = translator(delete="abcd", keep="cdef")
    print(trans('abcdef'))