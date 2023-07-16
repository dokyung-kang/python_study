# 내가 푼 문제

arr = "aaabbcccccca"
nArr = []

before = arr[0]
cnt = 0
for a in arr:
    if before != a:
        nArr.append(before)
        nArr.append(str(cnt))
        before = a
        cnt = 1
    else:
        cnt += 1

nArr.append(a)
nArr.append(str(cnt))

print("".join(nArr))