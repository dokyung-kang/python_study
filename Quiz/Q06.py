# 내가 푼 문제

numStr = input()
num = numStr.split(',')
total = 0

for i in num:
    total += int(i);
print(total)