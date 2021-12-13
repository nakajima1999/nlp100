#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第3章: 正規表現
# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

import nlp100_20

if __name__ == '__main__':
    # 「イギリス」に関する記事本文
    text_uk = nlp100_20.get_text_uk()
    print(text_uk)