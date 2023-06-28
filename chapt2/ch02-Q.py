# 연습 문제

## Q1.
korean = 80
english = 75
math = 55
total = korean + english + math
avg = (total) / 3
print(avg)


## Q2.
num = 13
answer = (num % 2 == 0)
print(answer)


## Q3.
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)


## Q4.
pin = "881120-1068234"
print(pin[7])


## Q5.
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)


## Q6.
a = [1, 2, 3, 4, 5]
a.sort()
a.reverse()
print(a)


## Q7.
a = ['life', 'is', 'to', 'short']
result = a[0] + " " + a[1] + " " + a[2] + " " + a[3]
print(result)

### A7.
result = " ".join(a)
print(result)


## Q8.
a = (1, 2, 3)
a = a + (4,)
print(a)


## Q9.

### A7. 3번 - 딕셔너리의 키로 변하는 값을 사용할 수 없음


## Q10.
A = {'A': 90, 'B': 80, 'C': 70}
result = A['B']
print(A)
print(result)

### A10. 
result = A.pop('B')
print(a)
print(result)


## Q11.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)


## Q12.
### b값도 a값과 같아짐
### 같은 객체를 가리킴
