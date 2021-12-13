#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第3章: 正規表現
###########################################################################################################
# Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
# 1行に1記事の情報がJSON形式で格納される
# 各行には記事名が”title”キーに，記事本文が”text”キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
# ファイル全体はgzipで圧縮される
# 以下の処理を行うプログラムを作成せよ．
############################################################################################################

import json

def get_text_uk():
    f_in = 'jawiki-country.json'
    with open(f_in, mode='r') as f:
        for line in f:
            line = json.loads(line)
            
            # タイトルが「イギリス」のデータを抽出
            if line['title'] == 'イギリス':
                # イギリスに関する記事本文を抽出
                text_uk = line['text']
                break
    return text_uk