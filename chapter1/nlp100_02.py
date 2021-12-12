#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 第1章: 準備運動
# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ
p = 'パトカー'
t = 'タクシー'
ans = ''
for a, b in zip(p, t):
    ans += a + b
print(ans)