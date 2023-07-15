# 내가 푼 문제

f = open("abc.txt", 'r')
str = f.readlines()
f.close()
str.reverse()
f = open("abc.txt", 'w')
for n in str:
    n = n.strip()
    f.write(n)
    f.write('\n')
f.close()