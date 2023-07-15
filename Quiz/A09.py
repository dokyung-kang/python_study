# 정답

f = open("sample1.txt")
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score
average = total / len(lines)

f = open("result1.txt", "w")
f.write(str(average))
f.close()