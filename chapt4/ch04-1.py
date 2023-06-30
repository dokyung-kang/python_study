# 파이썬 함수의 구조

## 예1
def add(a, b):
    return  a + b

a = 3
b = 4
c = add(a, b)
print(c)



### 매개변수와 인수
def add(a, b):
    return a + b
print(add(3, 4))



# 입력값과 결괏값에 따른 함수의 형태

## 일반적인 함수
def add(a, b):
    result = a + b
    return result
a = add(3, 4)
print(a)


## 입력값이 없는 함수
def say():
    return  'Hi'
a = say()
print(a)


## 결괏값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
add(3, 4)
a = add(3, 4)
print(a)


## 입력값도 결괏값도 없는 함수
def say():
    print('Hi')
say()



# 매개변수 지정하여 호출하기

## 예1
def add(a, b):
    return a+b
result = add(a=3, b=7)
print(result)
result = add(a=5, b=3)
print(result)



# 입력값이 몇 개가 될지 모르 때는 어떻게 해야 할까?

## 여러 개의 입력값을 받는 함수 만들기

### 예1
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1, 2, 3)
print(result)
result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

### 예2
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)

result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

### 점프 투 파이썬 - 키워드 파라미터
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)



# 함수의 결괏값은 언제나 하나이다

## 예1
def add_and_mul(a, b):
    return a+b, a*b

result = add_and_mul(3, 4)
print(result)

result1, result2 = add_and_mul(3, 4)
print(result1)
print(result2)

## 예2
def add_and_mul(a, b):
    return a+b
    return a*b

result = add_and_mul(2, 3)
print(result)

### 점프 투 파이썬 - return의 또 다른 쓰임새
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." % nick)

say_nick('야호')
say_nick('바보')



# 매개변수에 초깃값 미리 정하기

## 예1
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응용", 27, False)



# 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a + 1
vartest(a)
print(a)

def vartest(hello):
    hello = hello + 1
vartest(3)
print(a)


## 함수 안에서 함수 밖의 변수를 변경하는 방법

### return 사용하기
a = 1
def vartest(a):
    a = a + 1
    return a
a = vartest(a)
print(a)


## global 명령어 사용하기
a = 1
def vartest():
    global a
    a = a + 1
vartest()
print(a)



# lambda
add = lambda a, b: a+b
result = add(3, 4)
print(result)

def add(a, b):
    return a+b
result = add(3, 4)
print(result)