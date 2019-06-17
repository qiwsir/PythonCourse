#coding:utf-8

class SchoolKid:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name):
        self.name = new_name
        return self.name
    def change_age(self, new_age):
        self.age = new_age
        return self.age
    def get(self, attr='name'):
        if attr == "name":
            return self.name
        elif attr == "age":
            return self.age
        else:
            print("there is not ", attr)
            return None

class ExaggeratingKid(SchoolKid):
    def get(self, attr='name'):
        if attr == 'name':
            return self.name
        elif attr == 'age':
            return self.age + 12
        else:
            print("there is not ", attr)
            return None
baby = ExaggeratingKid("Tom", 2)
print(baby.get('age'))