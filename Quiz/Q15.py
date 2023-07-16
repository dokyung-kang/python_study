# 내가 푼 문제

def dupNum(arr):
    nArr = []

    for a in arr:
        if a not in nArr:
            nArr.append(a)
        else:
            return False

    return True

print(dupNum("0123456789"))
print(dupNum("01234"))
print(dupNum("01234567890"))
print(dupNum("6789012345"))
print(dupNum("012322456789"))
