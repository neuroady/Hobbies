#!bin/bash
for file in $(ls ./images/)
do python GenNonogram.py ./images/$file
	echo "--------------------------------------------------------"
done
