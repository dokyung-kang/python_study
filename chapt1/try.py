#파이썬 기초 문법 따라 해 보기

## 사칙연산
### 더하기
print(1 + 2)
### 나눗셈과 곱셉
print(3 / 2.4)
print(3 * 9)

## 변수에 숫자 대입하고 계산하기
a = 1
b = 2
print(a + b)

## 변수에 문자 대입하고 출력하기
a = "Python"
print(a)

## 조건문 if
a = 3
if a > 1:
    print("a is greater than 1")
    
## 반복문 for
for a in [1, 2, 3]:
    print(a)

## 반복문 while
i = 0
while i < 3:
    i = i + 1
    print(i)

## 함수
def add(a, b):
    return a + b
print(add(3, 4))

## 여러 줄짜리 주석문
"""
여러 줄로 이루어진 주석은 큰따옴표 세 개를 연속으로 사용한 기호 사이에 주석문을 작성하면 된다. 
큰 따옴표 대신 작은 따옴표 세 개(''')를 사용해도 된다. 
"""