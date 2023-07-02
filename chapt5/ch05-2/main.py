# 모듈 만들기

## 예1
import mod1_1
print(mod1_1.add(3, 4))
print(mod1_1.sub(4, 2))


## 예2
from mod1_1 import add
print(add(3, 4))



# if __name__ == "__main__"의 의미

## 예1 - if __name__ == "__main__" 없음
import mod1_2


## 예2 if __name__ == "__main__" 있음
import mod1_2


## 예3
from mod1_1 import add, sub


## 예4
from  mod1_1 import *



# 클래스나 변수 등을 포함한 모듈

## 예1
import mod2
print(mod2.PI)


## 예2
a = mod2.Math()
print(a.solv(2))


## 예3
print(mod2.add(mod2.PI, 4.4))


# 나 혼자 코딩!
## mod2.py 모듈을 사용해 반지름이 5인 원의 넓이를 계산해보자
import mod2
a = mod2.Math()
print(a.solv(5))
