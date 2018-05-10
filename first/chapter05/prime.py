#coding:utf-8
'''
    choose the prime number.
    filename: prime.py
'''

import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def choice_prime(*args):
    primes = [i for i in args if is_prime(i)]
    return primes

p = choice_prime(1,3,5,7,9,11,13,15,17,19,21,23)
print(p)