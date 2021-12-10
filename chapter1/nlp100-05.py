#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第1章: 準備運動
# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
def get_n_gram(sequence, n):
    list_ngram = []
    for i in range(len(sequence) - n + 1):
        list_ngram.append(sequence[i:i+n])
    
    return list_ngram
s = 'I am an NLPer'  # 文字列
list_word = s.split()  # リスト
list_ngram_chr = get_n_gram(s, 2)  # 文字bi-gram
list_ngram_word = get_n_gram(list_word, 2)  # 単語bi-gram
print('文字bi-gram:', list_ngram_chr)
print('単語bi-gram:', list_ngram_word)