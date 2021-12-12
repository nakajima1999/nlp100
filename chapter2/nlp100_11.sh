#!/bin/sh
cat popular-names.txt | sed -e 's/\t/ /g' > space_sed.txt
cat popular-names.txt | tr '\t' ' ' > space_tr.txt
expand -t4 popular-names.txt > space_expand.txt

