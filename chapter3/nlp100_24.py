#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第3章: 正規表現
# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

import nlp100_20
import re

if __name__ == '__main__':
    # 「イギリス」に関する記事本文
    text_uk = nlp100_20.get_text_uk()

    # 記事から参照されているメディアファイル
    pattern = r'\[\[(ファイル|File):([^]|]+?)(\|.*?)+\]\]'
    
    # 結果をすべて格納するリスト
    all_result = re.findall(pattern, text_uk)

    # 1件ずつ結果を出力
    for result in all_result:
        media_file = result[1]  # メディアファイル
        print(media_file)