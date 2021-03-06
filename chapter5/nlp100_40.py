#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第5章: 係り受け解析
###########################################################################################################
# 日本語Wikipediaの「人工知能」に関する記事からテキスト部分を抜き出したファイルがai.ja.zipに収録されている． 
# この文章をCaboChaやKNP等のツールを利用して係り受け解析を行い，その結果をai.ja.txt.parsedというファイルに保存せよ．
# このファイルを読み込み，以下の問に対応するプログラムを実装せよ．
###########################################################################################################

# 40. 係り受け解析結果の読み込み（形態素）
# 形態素を表すクラスMorphを実装せよ．
# このクラスは表層形（surface），基本形（base），品詞（pos），
# 品詞細分類1（pos1）をメンバ変数に持つこととする．
# さらに，係り受け解析の結果（ai.ja.txt.parsed）を読み込み，
# 各文をMorphオブジェクトのリストとして表現し，冒頭の説明文の形態素列を表示せよ．