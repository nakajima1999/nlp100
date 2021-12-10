#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第2章: UNIXコマンド
# 11. タブをスペースに置換Permalink
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
f_in = 'popular-names.txt'
f_out = 'space.txt'
count_lines = 0
with open(f_in) as f, open(f_out, 'w') as f2:
    for line in f:
        out_line = line.replace('\t', ' ')
        f2.write(out_line)