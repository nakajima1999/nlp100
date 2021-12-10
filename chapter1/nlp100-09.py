#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第1章: 準備運動
# 9. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば”I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．

import random

def typoglycemia(s):
    list_result = []
    words = s.split()
    for word in words:
        if len(word) <= 4:
            list_result.append(word)
        else:
            list_result.append(word[0] + ''.join(random.sample( word[1:-1], len(word[1:-1]))) + word[-1])   
    result = ' '.join(list_result)          
    return result

s = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
print(s)
print(typoglycemia(s))