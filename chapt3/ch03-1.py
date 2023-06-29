# if문은 왜 필요할까?

## 예1
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")



# 조건문이란 무엇인가?

## 비교 연산자

### 예1
x = 3
y = 2
print(x > y)
print(x < y)
print(x == y)
print(x != y)

### 예2
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


## and, or, not

### 예1
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


## x ins s, not in s

### 예1
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

### 예2
print('a' in ('a', 'b', 'c'))
print('j' not in 'puthon')

### 예3
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
    
# 나 혼자 코딩!
## '주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고 가라'는 문장을 조건문으로 만들어 보자.
if 'card' in pocket:
    print("버스를 타고 가라")
else:
    print("걸어 가라")

### 점프 투 파이썬 - 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")



# 다양한 조건을 판단하는 elif

## 예1
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")


## 예2
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")

### 점프 투  파이썬 - if문을 한 줄로 작성하기
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")



# 조건부 표현식

## 기존
score = 60
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)


## 조건부 표현식으로 바꾸기
score = 40
message = "success" if score >= 60 else "failure"
print(message)