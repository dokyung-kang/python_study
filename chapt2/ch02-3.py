# 리스트는 어떻게 만들고 사용할까?

## 간단한 표현
odd = [1, 3, 5, 7, 9]


## 리스트 생김새
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'life', 'is']
e = [1, 2, ['Life', 'is']]



# 리스트의 인덱싱과 슬라이싱

## 리스트의 인덱싱

### 예1
a = [1, 2, 3]
print(a)

### 예2 - 첫 번째 요소값
print(a[0])

### 예3 - 덧셈
b = a[0] + a[2]
print(b)

### 예4 - 마지막 요소값
print(a[-1])

### 예5 - 다른 리스트 포함
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])

### 예6 - 리스트 안 리스트 값
print(a[-1][0])

### 예7
print(a[-1][1])
print(a[-1][2])

### 예8
a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])


## 리스트의 슬라이싱

### 예1
a = [1, 2, 3, 4, 5]
print(a[0:2])

### 예2
a = "12345"
print(a[0:2])

### 예3
a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b)
print(c)


# 나 혼자 코딩!
## A = [1, 2, 3, 4, 5] 리스트에서 슬라이싱 기법을 사용하여 리스트 [2, 3]를 만들어 보자.
A = [1, 2, 3, 4, 5]
B = A[1:3]
print(B)


### 중첨된 리스트에서 슬라이싱
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])



# 리스트 연산하가

## 리스트 더하기 (+)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)


## 리스트 반복하기 (*)
a = [1, 2, 3]
print(a * 3)


## 리스트 길이 구하기
a = [1, 2, 3]
b = len(a)
print(b)

### 초보자가 실수하기 쉬운 리스트 연산 오류
a = [1, 2, 3]
b = str(a[2]) + "hi"        # 숫자를 문자로 바꿔야 합쳐야 함
print(b)



# 리스트의 수정과 삭제

## 리스트에서 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)


## del 함수 사용해 리스트 요소 삭제하기
a = [1, 2, 3]
del a[1]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)



# 리스트 관련 함수

## 리스트에 요소 추가 (append)
a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6])
print(a)


## 리스트 정렬 (sort)
a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)


## 리스트 뒤집기 (reverse)
a = ['a', 'c', 'b']
a.reverse()
print(a)


## 위치 반전 (index) - 존재하지 않으면 오류
a = [ 1, 2, 3]
a1 = a.index(3)
print(a1)

a2 = a.index(1)
print(a2)


## 리스트에 요소 삽입 (insert)
a = [1, 2, 3]
a.insert(0, 4)
print(a)

a.insert(3, 5)
print(a)


## 리스트 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

a.remove(3)
print(a)


## 리스트 요소 끄집어내기 (pop)
a = [1, 2, 3]
a1 = a.pop()
print(a1)
print(a)

a = [1, 2, 3]
a2 = a.pop(1)
print(a2)
print(a)


## 리스트에 포함된 요소 x의 개수 세기(count)
a = [1, 2, 3, 1]
b = a.count(1)
print(b)


## 리스트 확장 (extend)
a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6, 7]
a.extend(b)
print(a)            # a.extend([4, 5]) == a += [4, 5]