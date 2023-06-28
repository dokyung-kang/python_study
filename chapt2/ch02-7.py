# 불 자료형이란?

## 예1
a = True
b = False


## 예2
a1 = type(a)
print(a1)
b1 = type(b)
print(b1)


## 예3
print(1 == 1)
print(2 > 1)
print(2 < 1)



# 자료형의 참과 거짓

## 예1 - 거짓 프로그램
a = [1, 2, 3, 4]
while a:
    a.pop()


## 예2
if []:
    print("참")
else:
    print("거짓")


## 예3
if [1, 2, 3]:
    print("참")
else:
    print("거짓")



# 불 연산

## 예1
a = bool('python')
print(a)


## 예2
b = bool('')
print(b)


## 예3
a1 = bool([1, 2, 3])
print(a1)
a2 = bool([])
print(a2)
a3 = bool(0)
print(a3)
a4 = bool(3)
print(a4)