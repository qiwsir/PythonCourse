#coding:utf-8

'''
    about decorate
    filename: decorate.py
'''

def p_decorate(func):
    def wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return wrapper

def div_decorate(func):
    def wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return wrapper

@div_decorate
@p_decorate
def book(name):
    return "the name of book is {0}".format(name)

#my_book = p_decorate(book)
#result = my_book("PYTHON")
result = book("PYTHON")
print(result)