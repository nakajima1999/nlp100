#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第2章: UNIXコマンド
# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

import pandas as pd

f_in = 'popular-names.txt'
df = pd.read_csv(f_in, sep='\t', header=None)
df[0].to_csv('col1.txt', index=False, header=None)
df[1].to_csv('col2.txt', index=False, header=None)