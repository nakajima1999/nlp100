#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第2章: UNIXコマンド
# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

import pandas as pd

f_col1 = 'col1.txt'
f_col2 = 'col2.txt'

df_col1 = pd.read_csv(f_col1, sep='\t', header=None)
df_col2 = pd.read_csv(f_col2, sep='\t', header=None)

# col1とcol2を結合
df_merge = pd.concat([df_col1, df_col2], axis=1)  # axis=1とすると横方向に連結される
df_merge.to_csv('merge.txt', sep='\t', index=False, header=None)

