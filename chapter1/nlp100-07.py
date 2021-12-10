#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第1章: 準備運動
# 07. テンプレートによる文生成
# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．
def get_tmp_snt(x, y, z):
    s = '{}時の{}は{}'.format(x, y, z)
    return s

 
x = 12
y = "気温"
z = 22.4
print(get_tmp_snt(x, y, z))
