#coding:utf-8

class Student:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    
    def eat(self, food):
        if food == 'meat':
            price = 10
        else:
            price = 5
        return price

    def learn(self, *subjects):
        if "python" in subjects:
            return "前程似锦"
        else:
            return "是且仅是道路曲折"

boy = Student('laoqi', 'physics')
print(boy.department)
subj = boy.learn('chinese', 'english', 'physics', 'algrathm')
print(subj) 