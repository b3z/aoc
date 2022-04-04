wc -c input.txt

vim:
:%s/^"//g
:%s/"$//g
:%s/\\"/"/g
:%s/\\\\/\\/g
:%s/\\x[a-fA-F0-9][a-fA-F0-9]/-/g

wc -c input-non.txt

subtract the results and add one for newline

6609-5277 + 1 = 1333

part 2:

printf "%q" $(cat input.txt) | wc -c
wc -l
add 2*300 quotes

8055 + 600 - 6609 = 2046
