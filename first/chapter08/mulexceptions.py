# coding=utf-8
'''
    handling multiple exceptions.
    filename: mulexceptions.py
'''

while True:    
    try:
        a = float(input("first number: "))
        b = float(input("second number: "))
        r = a / b
        print("{0} / {1} = {2}".format(a, b, r))
        #break
    except (ZeroDivisionError, ValueError) as e:
        print(e)
        print("Try again.")
    # except ZeroDivisionError:
    #     print("The second numbers can not be zero. Try again.")
    # except ValueError:
    #     print("Please enter number. Try again.")
    else:
        break