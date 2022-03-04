#!bin/bash
for file in $(ls ./images/)
do python GenNonogram.py $file
	echo "--------------------------------------------------------"
done
