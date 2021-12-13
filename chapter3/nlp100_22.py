#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第3章: 正規表現
# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import nlp100_20
import re

if __name__ == '__main__':
    # 「イギリス」に関する記事本文
    text_uk = nlp100_20.get_text_uk()

    # カテゴリ名を宣言している行
    pattern = '\[\[Category:(.+)\]\]'

    k = 0
    for line in text_uk.split('\n'):
        if re.search(pattern, line):
            result = re.match(pattern, line)

            # カテゴリ名を抽出
            result = result.group(1)

            # 余計な部分を空文字で置換
            result = result.replace('|*', '').replace('|元', '')
            
            # 結果を表示
            print(result)
      