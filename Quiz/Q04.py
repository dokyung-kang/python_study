# 내가 푼 문제

A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
total = 0

for i in range(0, len(A)):
    if A[i] >= 50:
        total += A[i]

print(total)
