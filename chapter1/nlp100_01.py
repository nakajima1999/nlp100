#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第1章: 準備運動
# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ
s = 'パタトクカシーー'
n = [1,3,5,7]
t = ''.join([s[i - 1] for i in n])
print(s)
print(t)