# coding:utf-8

'''
    create a class
    filename: superman.py
'''

class SuperMan:
    '''
    A class of superman
    '''
    def __init__(self, name):
        self.name = name
        self.gender = 1    #1: male
        self.single = False
        self.illness = False

    def nine_negative_kungfu(self):
        return "Ya! You have to die."

zhangsan = SuperMan("zhangsan")
print("superman's name is:", zhangsan.name)
print("superman is:(0-female, 1-male) ",zhangsan.gender)
result = zhangsan.nine_negative_kungfu()
print("If superman play nine negative kungfu, the result is:")
print(result)