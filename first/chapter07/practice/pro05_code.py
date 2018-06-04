#coding:utf-8

s = '''
You raise me up, so I can stand on mountains
You raise me up to walk on stormy seas
I am strong when I am on your shoulders
You raise me up to more than I can be
'''
words = s.split()
#print(words)

from collections import Counter
words_counts = Counter(words)
top3 = words_counts.most_common(3)
print(top3)