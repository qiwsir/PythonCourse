# coding=utf-8
'''
    the example code of encapsulation
    filename: private.py
'''

class ProtectMe: 
    def __init__(self):
        self.me = "qiwsir"
        self.__name = "laoqi"

    def __python(self):
        print("I love Python.")

    def code(self):
        print("Which language do you like?")
        self.__python()

p = ProtectMe()
p.code()
print(p.me)
#print(p.__name)
p.__python()