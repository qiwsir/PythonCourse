# coding:utf-8
'''
    Your name and age.
    filename: name.py
'''
name = input("What is your name?")
age = input("How old are you?")

after_ten = int(age) + 10

print("-" * 20)
print("Your name is: ",  name)
print("You are " + age + " years old.")
print("You will be " + str(after_ten) + " years old after ten years.")
