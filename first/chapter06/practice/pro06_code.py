#coding:utf-8
'''
6. 写一个类，用阿拉伯数字实例化之后，能够得到相应的罗马数字。
'''

class IntRoman:
    # val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    # syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    ROMAN = [
    (1000, "M"),
    ( 900, "CM"),
    ( 500, "D"),
    ( 400, "CD"),
    ( 100, "C"),
    (  90, "XC"),
    (  50, "L"),
    (  40, "XL"),
    (  10, "X"),
    (   9, "IX"),
    (   5, "V"),
    (   4, "IV"),
    (   1, "I"),]

    def __init__(self, n):
        self.n = n
    
    # method 1
    def arabic2roman(self):
        number = self.n
        result = ""
        for (arabic, roman) in self.ROMAN:
            (factor, number) = divmod(number, arabic)
            result += roman * factor
        return result
    
    # method 2
    # def get_roman(self):
    #     num = self.n
    #     roman_num = ''
    #     i = 0
    #     while  num > 0:
    #         for _ in range(num // self.val[i]):
    #             roman_num += self.syb[i]
    #             num -= self.val[i]
    #         i += 1
    #     return roman_num


a = IntRoman(1024)
print(a.arabic2roman())
# print(py_solution().int_to_Roman(1))
# print(py_solution().int_to_Roman(4000))
