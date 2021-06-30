import hashlib

def hash(s):
    return hashlib.md5(s.encode()).hexdigest()


input = "iwrupvqb"
#input = "abcdef" # expect 609043
#input = "pqrstuv" # expect 1048970
num = 0
res = hash(input)

while res[:6] != "000000":
    res = hash(input+str(num))
    num += 1
    print(res)

print(f'Result: {input} {str(num-1)}')


