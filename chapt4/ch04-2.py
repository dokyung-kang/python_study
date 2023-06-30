# 사용자 입력

## input의 사용
a = input()
print(a)


## 프롬프트 값을 띄워서 사용자 입력받기
number = input("숫자를 입력하세요:")
print(number)



# print 자세히 알기

## print 사용 예
a = 123
print(a)

a = "Python"
print(a)

a = [1, 2, 3]
print(a)


## 큰따옴표(")로 둘러싸인 문자열은 +연산과 동일하다
print("Life" "is" "too short")
print("Life"+"is"+"too short")


## 문자열 띄어쓰기는 콤마로 한다
print("Life", "is", "too short")


## 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=' ')