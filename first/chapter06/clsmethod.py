#coding:utf-8
'''
    learn class method.
    filename: clsmethod.py
'''

class Message:
    msg = "Python is a smart language."

    def get_msg(self):
        print("the self is:", self)
        print("attrs of class(Message.msg):", Message.msg)

    @classmethod
    def get_cls_msg(cls):
        print("the cls is:", cls)
        print("attrs of class(cls.msg):", cls.msg)

mess = Message()
mess.get_msg()
print("-" * 10)
mess.get_cls_msg()