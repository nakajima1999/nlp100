#!/bin/sh

# プロンプトをechoを使って表示
echo -n INPUT_STR: 
# 入力を受付、その入力を「str」に代入
read n 

# 末尾のN行だけを表示
tail -n $n popular-names.txt