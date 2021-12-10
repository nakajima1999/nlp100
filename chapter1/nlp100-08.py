#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第1章: 準備運動
# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
## - 英小文字ならば(219 - 文字コード)の文字に置換
## - その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(s):
    result = ''
    for i in range(len(s)):
        if 97 <= ord(s[i]) <=122:
            result += chr(219 - ord(s[i]))
        else:
            result += s[i]
    return result

s = 'the quick brown fox jumps over the lazy dog'
print('元の文: {}'.format(s))
print('暗号化: {}'.format(cipher(s)))
print('復号化: {}'.format(cipher(cipher(s))))