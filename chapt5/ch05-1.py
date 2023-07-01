# 클래스는 왜 필요한가?

## 예1 - 계산기 1개
result = 0
def add(num):
    global result
    result += num
    return result
print(add(3))
print(add(4))


## 예2 - 계산기 2개
result1 = 0
result2 = 0
def add1(num):
    global result1
    result1 += num
    return result1
def add2(num):
    global result2
    result2 += num
    return result2
print(add1(3))
print(add1(3))
print(add2(3))
print(add2(7))


## 예3 - 클래스
class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))



# 사칙연산 클래스 만들기

## 클래스 구조 만들기
class FourCal:
    pass
a = FourCal()
print(type(a))


## 객체에 숫자 지정할 수 있게 만들기
class FourCal:
    def setData(self, first, second):
        self.first = first
        self.second = second

### setdata 메서드의 매개변수
a = FourCal()
a.setData(4, 2)

### 점프 투 파이썬 - 메서드의 또 다른 호출 방법
a = FourCal()
FourCal.setData(a, 4, 2)

### setdata 메서드의 수행문
#### a.setdata(4, 2)
#### self.first = 4 == a.first = 4
#### self.second = 2 == a.second = 2
a = FourCal()
a.setData(4, 2)
print(a.first)
print(a.second)

a = FourCal()
b = FourCal()
a.setData(4, 2)
print(a.first)
b.setData(3, 7)
print(b.first)

#### 객체변수 독립적인 값을 유지
a = FourCal()
b = FourCal()
a.setData(4, 2)
b.setData(3, 7)
print(id(a.first))
print(id(b.first))


## 더하기 기능 만들기
class FourCal:
    def setData(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
a = FourCal()
a.setData(4, 2)
print(a.add())


## 곱하기, 빼기, 나누기 기능 만들기
class FourCal:
    def setData(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal()
b = FourCal()
a.setData(4, 2)
b.setData(3, 8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())



# 생성자(Constructor)
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setData(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal(4, 2)
print(a.first)
print(a.second)
print(a.add())
print(a.div())



# 클래스의 상속

## 간단 상속
class MoreFourCal(FourCal):
    pass
a = MoreFourCal(4, 2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())


## a의 b제곱
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4, 2)
print(a.pow())


## 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
a = SafeFourCal(4, 0)
print(a.div())



# 클래스 변수

## 클래스 예1
class Family:
    lastname = "김"
print(Family.lastname)
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)


## 클래스 예2
class Family:
    lastname = "박"
print(Family.lastname)
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)
print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))
