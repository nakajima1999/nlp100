#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第2章: UNIXコマンド
# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
f_in = 'popular-names.txt'
count_lines = 0
with open(f_in) as f:
    for line in f:
        count_lines += 1
print(count_lines)
