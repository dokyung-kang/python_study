# 집합 자료형은 어떻게 만들까?

## 예1 - set 키워드
s1 = set([1, 2, 3])
print(s1)


## 예2 - 문자열
s2 = set("Hello")
print(s2)



# 집합 자료형의 특징

## 예1 - 리스트 변환
s1 = set([1, 2, 3])
li = list(s1)
print(li)


## 튜플로 변환
t1 = tuple(s1)
print(t1)
print(t1[0])



# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

## 교집합
a1 = s1 & s2
print(a1)

a2 = s1.intersection(s2)
print(a2)


## 합칩합
a1 = s1 | s2
print(a1)

a2 = s1.union(s2)
print(a2)


## 차집합
a1 = s1 - s2
print(a1)
a2 = s2 - s1
print(a2)

a3 = s1.difference(s2)
print(a3)
a4 = s2.difference(s1)
print(a4)



# 집합 자료형 관련 함수

## 값 1개 추가하기 (add)
s1 = set([1, 2, 3])
s1.add(4)
print(s1)


## 값 여러 개 추가하기 (update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)


## 특정 값 제거하기 (remove)
s1 = ([1, 2, 3])
s1.remove(2)
print(s1)