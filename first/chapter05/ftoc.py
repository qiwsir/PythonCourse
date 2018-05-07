#coding:utf-8
'''
    convert temperature between F and C
    filename: ftoc.py
'''

def convertfc(f=None, c=None):
    if f:
        c = (f - 32) * 5 / 9
        return round(c, 2)
    if c:
        f = c * 9 / 5 + 32
        return round(f, 2)

    if f and c:
        return None

temp = input('input the number of temperature(f=32, or c = 32):')
u = temp[0]
n = temp.split('=')[-1]
if u == 'c':
    result = convertfc(c=int(n))
    print('convert Celsius to Fahrenheit. {0}°C => {1}°F'.format(n, result))
if u == 'f':
    result = convertfc(f=int(n))
    print('convert Fahrenheit to Celsius. {0}°F => {1}°C'.format(n, result))