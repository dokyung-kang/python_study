# 내가 푼 문제

#arr = input()
arr = "4546793"

oriStr = list(map(int, arr))
newStr = []


for i, n in enumerate(oriStr):
    tmp = str(n)
    newStr.append(tmp)
    if i < len(oriStr) - 1:
        if n % 2 == 1:
            odd = 1
        else:
            odd = 0
        if oriStr[i + 1] % 2 == 1:
            nOdd = 1
        else:
            nOdd = 0
        if odd == 1 and nOdd == 1:
            newStr.append("-")
        if odd == 0 and nOdd == 0:
            newStr.append("*")

print("".join(newStr))