#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第3章: 正規表現
# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import nlp100_20
import re

if __name__ == '__main__':
    # 「イギリス」に関する記事本文
    text_uk = nlp100_20.get_text_uk()

    # カテゴリ名を宣言している行
    pattern = '\[\[Category:.*\]\]'

    k = 0
    for line in text_uk.split('\n'):
        if re.search(pattern, line):
            # 結果を表示
            print(line)
