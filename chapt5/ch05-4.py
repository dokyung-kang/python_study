# 오류 예외 처리 기법

## try, except문
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# 나 혼자 코딩!
## 앞에서 나온 3번 방법을 사용해 IndexError가 발생할 때 오류 메세지를 출력하는 소스를 작성해 보자.
a = [1, 2, 3]
try:
    print(a[4])
except IndexError as e:
    print(e)


## try ... finally

### 예1
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")

### 예2
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

### 예3
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)



# 오류 회피하기
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass



# 오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()



# 예외 만들기
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

## 예1
try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않은 별명입니다.")


## 예2
class MyError(Exception):
    def __str__(self):
        return "허용되지 않은 별명입니다."

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)