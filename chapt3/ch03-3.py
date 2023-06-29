# for문의 기본 구조

## 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)


## 다양한 for문의 사용
a = [(1,2), (3, 4), (5, 6)]
for (first , last) in a:
    print(first + last)


## for문의 응용
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)



# for문과 continue문
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % number)



# for문과 함께 자주 사용하는 range 함수

## 예1
a = range(10)
print(a)


## 예2
a = range(1, 11)
print(a)


## range 함수의 예시 살펴보기
add = 0
for i in range(1, 11):
    add = add + i
print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

# 나 혼자 코딩!
## for문과 range 함수를 사용하여 1부터 10까지 더해 보자
total = 0
for i in range(1, 101):
    total += i
print(total)


## for와 range를 사용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')



# 리스트 내포 사용하기

## 기본
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)


## 예1
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)


## 예2
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)


## 예3
result = [x*y for x in range(2, 10)
          for y in range(1, 10)]
print(result)