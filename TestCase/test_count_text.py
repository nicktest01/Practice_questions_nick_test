# -*- coding:utf-8 -*-
"""
買字母貼紙來布置活動空間，文字為"Hello welcome to year anniversary"，
請寫一個程式計算每個字母(大小寫視為同個字母)出現次數
"""
#計算每個字母(大小寫視為同個字母)出現次數
from collections import defaultdict

def count_letters(text):
    letter_count = defaultdict(int)
    for char in text:
        if char.isalpha():
            char_lower = char.upper()
            letter_count[char_lower] += 1
    return letter_count

text = "Hello welcome to year anniversary"
letter_counts = count_letters(text)

# 依照要求的格式輸出字母及其出現次數
for letter, count in sorted(letter_counts.items()):
    print(f"{letter} {count}")

