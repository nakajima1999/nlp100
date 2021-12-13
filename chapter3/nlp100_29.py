#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第3章: 正規表現
# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

import nlp100_20

if __name__ == '__main__':
    # 「イギリス」に関する記事本文
    text_uk = nlp100_20.get_text_uk()
    print(text_uk)