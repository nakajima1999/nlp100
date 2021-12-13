#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第3章: 正規表現
# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

import nlp100_20
import re

if __name__ == '__main__':
    # 「イギリス」に関する記事本文
    text_uk = nlp100_20.get_text_uk()

    # セクション名を宣言している行
    pattern = '^(=+)(.+?)(=+)$'

    k = 0
    for line in text_uk.split('\n'):
        if re.search(pattern, line):
            result = re.match(pattern, line)

            # セクション名とそのレベルを抽出
            lebel = len(result.group(1)) // 2  # レベル
            session = result.group(2).strip()  # セッション名

            # 結果を表示
            print(session, lebel)