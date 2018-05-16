#coding:utf-8
'''
    How to use property() in the programming.
    filename: propertyfunc.py
'''

class Book:
    def __init__(self, book_name='python'):
        self.__book_name = book_name

    @property
    def name(self):
        print('Getting book name.')
        return self.__book_name

    @name.setter
    def name(self, name):
        print('Setting book name.')
        self.__book_name = name

    #name = property(get_name, set_name)
    # name = property()
    # name = name.getter(get_name)
    # name = name.setter(set_name)

b = Book()
print(b.name)
b.name = 'Rust'
print(b.name)