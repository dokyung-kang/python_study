# 내가 푼 문제

total = 0

f = open("sample.txt", 'r')
strN = f.readlines()
f.close()
for n in strN:
    tmp = int(n)
    total += tmp

avg = total / 10

f = open("result.txt", 'w')
f.write(str(avg))
f.close()