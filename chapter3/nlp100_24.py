#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第3章: 正規表現
# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

import nlp100_20

if __name__ == '__main__':
    # 「イギリス」に関する記事本文
    text_uk = nlp100_20.get_text_uk()
    print(text_uk)