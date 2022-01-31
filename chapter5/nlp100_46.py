#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第5章: 係り受け解析
# 46. 動詞の格フレーム情報の抽出
# 45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
# 45の仕様に加えて，以下の仕様を満たすようにせよ．
# - 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない
# - 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる