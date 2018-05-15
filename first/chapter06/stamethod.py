#coding:utf-8

class Cat:
    ears = 2
    legs = 4
    def __init__(self, color):
        self.color = color

    @staticmethod
    def speak():
        print("Meow, Meow")

Cat.speak()
Cat("black").speak()

