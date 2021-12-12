#!/bin/sh

# プロンプトをechoを使って表示
echo -n INPUT_STR: 
# 入力を受付、その入力を「str」に代入
read $n

echo 

# ファイルをN分割する
split -l 200 popular-names.txt
