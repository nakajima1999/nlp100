#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第2章: UNIXコマンド
# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

import pandas as pd

f_in = 'popular-names.txt'
df = pd.read_csv(f_in, sep='\t', header=None)
df.columns = ['name', 'sex', 'number', 'year']
df.sort_values(by='number', ascending=False, inplace=True)

f_out = 'sort_col3.txt'
df.to_csv(f_out, sep='\t', index=False, header=None)

