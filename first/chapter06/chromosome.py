#coding:utf-8
'''
    Judge having a boy or girl by sex chromosome.
    filename: chromosome.py
'''
import random

class Father:
    def __init__(self):
        self.father_chromosome = 'XY'

    def father_do(self):
        print("Make money.")

class Mother:
    def __init__(self):
        self.mother_chromosome = "XX"

    def mother_do(self):
        print("Manage money.")

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def child_gender(self):
        fat = random.choice(self.father_chromosome)
        mot = 'X'
        chi = fat + mot
        if "Y" in chi:
            return 1
        return 0

p  = Child()
if p.child_gender():
    print('is a BOY.')
else:
    print("is a GIRL.")