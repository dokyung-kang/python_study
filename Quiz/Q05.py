# 내가 푼 문제

num = int(input())

n1 = 0
n2 = 1
n3 = 0

if num == 0:
    print(n1)
elif num == 1:
    print(n2)
else:
    while True:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        if n3 > num:
            break
        print(n3)