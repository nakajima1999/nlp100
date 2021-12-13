#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第3章: 正規表現
# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．

import nlp100_20

if __name__ == '__main__':
    # 「イギリス」に関する記事本文
    text_uk = nlp100_20.get_text_uk()
    print(text_uk)