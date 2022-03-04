#!bin/bash
for file in $(ls ./images/)
do python GenNonogram.py -b ./images/$file
	echo "--------------------------------------------------------"
done
