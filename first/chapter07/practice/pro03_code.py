#coding:utf-8
'''
3. datetime和calendar都是Python标准库中跟时间、日期相关的模块。请使用它们，计算上一个周五的日期，并以特定格式在控制台打印出来。
'''

import datetime, calendar

last_friday = datetime.date.today()
one_day = datetime.timedelta(days=1)
while last_friday.weekday() != calendar.FRIDAY:
    last_friday -= one_day
print(last_friday.strftime('%A, %d-%b-%Y'))