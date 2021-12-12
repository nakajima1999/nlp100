#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第2章: UNIXコマンド
# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

from os import environb
import pandas as pd
from collections import defaultdict

f_in = 'popular-names.txt'
df = pd.read_csv(f_in, sep='\t', header=None)
list_col1 = list(df[0])

dic_count = defaultdict(int)
for name in list_col1:
    dic_count[name] += 1

# 出現回数が多い順にソート
count_sorted = sorted(dic_count.items(), key=lambda x:x[1], reverse=True)

f_out = 'col1_count_sort.txt'
with open(f_out, 'w') as f:
    for e in count_sorted:
        name = e[0]  # 名前
        c = e[1]  # 出現回数

        # 出現回数と名前を出力
        s = str(c) + '\t' + name + '\n'
        f.write(s)