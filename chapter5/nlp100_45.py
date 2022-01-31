#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第5章: 係り受け解析
# 45. 動詞の格パターンの抽出
# 今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 
# 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． 
# ただし，出力は以下の仕様を満たすようにせよ．
# - 動詞を含む文節において，最左の動詞の基本形を述語とする
# - 述語に係る助詞を格とする
# - 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べ