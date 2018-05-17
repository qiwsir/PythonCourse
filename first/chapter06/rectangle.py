#coding:utf-8
'''
    define a type of rectangle.
    filename: rectangle.py
'''

class NewRectangle:
    def __init__(self):
        self.width = 0
        self.length = 0

    def __getattr__(self, name):
        if name == "size":
            return self.width, self.length
        else:
            raise AttributeError
        
    def __setattr__(self, name, value):
        if name == "size":
            self.width, self.length = value
        else:
            self.__dict__[name] = value


rect = NewRectangle()
rect.width = 3
rect.length = 4
print(rect.size)
print("--"*10)
rect.size = 30, 40
print("with:", rect.width)
print("length:", rect.length)