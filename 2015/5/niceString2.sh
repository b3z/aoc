cat input.txt |  grep "\(..\).*\1" | grep "\(.\).\1" >> res
wc res
rm res
