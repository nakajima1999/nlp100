#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第2章: UNIXコマンド
# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

f_in = 'popular-names.txt'
n = int(input())
with open(f_in) as f:
    lines = f.readlines()
    out_lines = lines[-n:]

for line in out_lines:
    print(line.strip())
