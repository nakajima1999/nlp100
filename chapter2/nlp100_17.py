#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第2章: UNIXコマンド
# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはcut, sort, uniqコマンドを用いよ．

import pandas as pd
f_in = 'popular-names.txt'
df = pd.read_csv(f_in, sep='\t', header=None)
set_col1 = set(df[0].unique())
print(set_col1)
print(len(set_col1))
