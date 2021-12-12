#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第2章: UNIXコマンド
# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

import pandas as pd

f_in = 'popular-names.txt'
n = int(input())
df = pd.read_csv(f_in, sep='\t', header=None)
p = len(df) // n  # ファイルの行数をN分割
q = len(df) % n  # あまり(あまりの分のファイルの行数はp+1行, それ以外のファイルの行数はp行)
k = 0

for i in range(n):
    if i < q:
        c = p + 1
    else:
        c = p

    f_name = 'split_' + str(n) + '_' + str(i + 1) + '.txt'  # ファイル名
    df[k:k + c].to_csv(f_name, sep='\t', index=False, header=None)
    k += c
