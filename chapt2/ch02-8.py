# 변수란?

## 예1 - 변수
a = [1, 2, 3]


## 예2 - 메모리 주소 확인
a = [1, 2, 3]
a1 = id(a)
print(a1)



# 리스트를 복사할 때

a = [1, 2, 3]
b = a


## 예1 - id() 동일
print(id(a))
print(id(b))


## 예2 - 가르키는 객체 동일
print(a is b)


## 예3
a[1] = 4
print(a)
print(b)


## [:] 사용
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)


## copy 모듈 사용
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(a)
print(b)
print(b is a)



# 변수를 만드는 여러 가지 방법

## 예1
a, b = ('python', 'life')
print(a)
print(b)


## 예2
(a, b) = 'python', 'life'
print(a)
print(b)


## 예3
[a, b] = ['python', 'life']


## 예4
a = b = 'python'


## 예5
a = 3
b = 5
a, b = b, a
print(a)
print(b)

# 나 혼자 코딩!
## 다음 예제를 실행하고 그 결과를 설명해보자.
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
### 메모리가 다르기 때문에 False