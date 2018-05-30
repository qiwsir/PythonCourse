#coding:utf-8
'''
2. 编写程序，在单词列表中查找包含所有元音字母“aeiou”的单词。
'''
def clean_word(word):
    return word.strip().lower()

def find_vowels_word(word):
    vowels = "aeiou"
    vowels_word = ""
    for char in word:
        if char in vowels:
            vowels_word += char
    return vowels_word

f = open("wordlist.txt")
result = []
for word in f:
    word = clean_word(word)
    if len(word) <= 5:
        continue
    vowels_str = find_vowels_word(word)
    if sorted(vowels_str) == 'aeiou':
        result.append(word)

print(result)