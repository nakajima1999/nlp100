#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第3章: 正規表現
# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import nlp100_20
import re

if __name__ == '__main__':
    # 「イギリス」に関する記事本文
    text_uk = nlp100_20.get_text_uk()

    # テンプレートの抽出
    pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
    template = re.findall(pattern, text_uk, re.MULTILINE + re.DOTALL)

    # フィールド名と値を辞書オブジェクトに格納
    col = template[0].split('\n|')  # 1件ずつ区切って，リストに格納

    # 「基礎情報」の辞書
    # key: フィールド名, value: 値
    dic_basic_info = {}
    for e in col:
        field = e.split('=')[0].strip()  # フィールド名
        value = e.replace(field, '').strip().lstrip('=').strip()  # 値
        if len(field) > 0 and len(value) > 0:
            dic_basic_info[field] = value
            print('{}:{}'.format(field, value))

# 結果を出力
print(dic_basic_info)