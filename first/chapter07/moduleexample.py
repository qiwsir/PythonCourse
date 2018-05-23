#coding:utf-8
'''
    The module of Python.
    filename: moduleexample.py
'''

class Book:
    lang = "python"
    
    def __init__(self, author):
        self.author = author

    def get_name(self):
        return self.author

def foo(x):
    return x * 2

# python = Book("laoqi")
# python_name = python.get_name()

# mul_result = foo(2)

__all__ = ['Book',]

if __name__ == "__main__":
    python = Book("laoqi")
    python_name = python.get_name()
    print(python_name)

    mul_result = foo(2)
    print(mul_result)

    print(__name__)