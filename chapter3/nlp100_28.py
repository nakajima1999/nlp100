#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第3章: 正規表現
# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

import nlp100_20

if __name__ == '__main__':
    # 「イギリス」に関する記事本文
    text_uk = nlp100_20.get_text_uk()
    print(text_uk)