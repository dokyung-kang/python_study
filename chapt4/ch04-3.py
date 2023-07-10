# 파일 생성하기
f = open("새파일1.txt", 'w')
f.close()


# 나 혼자 코딩!
## 복습.txt 파일을 C:/doit 디렉터리에 만들자
f = open("./복습1.txt", 'w')       # 현재 있는 위치로 바꿈



# 파일을 쓰기 모드로 열어 출력값 적기
f = open("새파일2.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)



# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법

## readline 함수 사용하기

### 한 줄
f = open("새파일2.txt", 'r')
line = f.readline()
print(line)
f.close()

### 모든 줄1
f = open("새파일2.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()


## readlines 함수 사용하기
f = open("새파일2.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()


## read 함수 사용하기
f = open("새파일2.txt", 'r')
data = f.read()
print(data)
f.close()



# 파일에 새로운 내용 추가하기
f = open("새파일2.txt", 'a')
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()

## 실행
f = open("새파일2.txt", 'r')
data = f.read()
print(data)
f.close()



# with문과 함께 사용하기

## 예1
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()


## 예2
with open("foo.txt", "w") as f:
    f.write("Life is too short, ypu need python")


### 점프 투 파이썬 - sys 모듈로 매개변수 주기

#### 예1
import sys
args = sys.argv[1:]
for i in args:
    print(i)

#### 예2
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')