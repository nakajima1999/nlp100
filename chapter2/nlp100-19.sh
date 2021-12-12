#!/bin/sh
cut -f 1 popular-names.txt | sort| uniq -c | sort -n -r > 'sh_col1_count_sort.txt'
