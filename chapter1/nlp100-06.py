#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第1章: 準備運動
# 06. 集合
# “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
def get_n_gram(sequence, n):
    list_ngram = []
    for i in range(len(sequence) - n + 1):
        list_ngram.append(sequence[i:i+n])
    
    return list_ngram
s = 'paraparaparadise'
t = 'paragraph'
X = set(get_n_gram(s, 2))
Y = set(get_n_gram(t, 2))

print('X:', X)
print('Y:', Y)
print('和集合:', X | Y)
print('積集合:', X & Y)
print('差集合:', X - Y)
print('差集合:', Y - X)