#!/bin/sh

# 各行を3コラム目の数値の降順にソート
# -r	--reverse	逆順で並べ替える
# -k 指定	--key=指定	場所と並べ替え種別を指定する（「-k 2」なら2列目、「-k 2n」なら2列目を数値として並べ替える。複数指定する場合は「-k」オプションを複数回指定する）
# -n	--numeric-sort	文字列を数値と見なして並べ替える
sort -r -k 3n popular-names.txt > sh_sort_col3.txt