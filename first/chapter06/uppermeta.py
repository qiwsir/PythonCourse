#coding:utf-8

class UpperMeta(type):
    def __new__(cls, name, bases, attrs):
        print("现在开始执行元类UpperMeta中的__new__")
        print("cls: ", cls)
        print("name: ", name)
        print("bases: ", bases)
        print("attrs: ", attrs)
        uppercase_attr = {}
        for name, value in attrs.items():
            if not name.startswith("__"):
                uppercase_attr[name.upper()] = value
            else:
                uppercase_attr[name] = value
        return type.__new__(cls, name, bases, uppercase_attr)
        #return super(UpperMeta, cls).__new__(cls, name, bases, uppercase_attr)

class Book(metaclass=UpperMeta):
    bookname = "Learn Python wit Laoqi"
    def __init__(self, name):
        print("现在开始执行类MyBook中的__init__")
        self.name = name
    def author(self):
        print("the book {0} author is {1}".format(self.book, self.name))

if __name__ == "__main__":
    print("-" * 20)
    bk = Book("laoqi")
    print(dir(bk))
