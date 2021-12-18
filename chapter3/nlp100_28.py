#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第3章: 正規表現
# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

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
        
        # 強調マークアップの除去
        pattern = r'\'{2,5}'
        value = re.sub(pattern, '', value)

        # 内部リンクマークアップの除去
        pattern = r'(\[\[.+?\]\])'
        all_result = re.findall(pattern, value)

        # 内部リンク
        # [[記事名]]
        # [[記事名|表示文字]]
        # [[記事名#節名|表示文字]]
        # 内部リンクを記事名か表示文字に変換する
        for result in all_result:
            rm_result = result[2:-2].split('|')[-1]  # 内部リンクマークアップの除去した後のテキスト
            value = value.replace(result, rm_result)

        # 外部リンクマークアップの除去
        # \w: 任意の英数字
        # ! ? / _ ~ = ; , * & @ # $ % 
        # + - . ( ) ' [ ]
        pattern = r'https?://[\w!?/_~=;,*&@#$%\+\-\.\(\)\'\[\]]+'
        value = re.sub(pattern, '', value)

        # HTMLタグの除去
        pattern = r'<.+?>' 
        value = re.sub(pattern, '', value)

        if len(field) > 0 and len(value) > 0:
            dic_basic_info[field] = value
            print('{}:{}'.format(field, value))

# 結果を出力
print(dic_basic_info)