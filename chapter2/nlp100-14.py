#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第2章: UNIXコマンド
# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

f_in = 'popular-names.txt'
n = int(input())
with open(f_in) as f:
    for i, line in enumerate(f):
        if i < n:
            print(line.strip())