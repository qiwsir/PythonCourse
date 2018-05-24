#coding:utf-8
'''
    keep speical characters in a string.
    filename: keeper.py
'''

class Keeper:
    def __init__(self, keep):
        self.keep = set(map(ord, keep))
    
    def __getitem__(self, n):
        if n not in self.keep:
            return None
        return chr(n)

    def __call__(self, s):
        return s.translate(self)


vowels = Keeper("aeiouy")
print(vowels("you raise me up."))