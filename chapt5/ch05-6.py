# 라이브러리
## sys
import sys
print(sys.argv)

### 강제로 스크립트 종료하기
# sys.exit()


### 자신이 만든 모듈 불러와 사용하기 - sys.path
import sys
print(sys.path)



## pickle

### 예1
import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)

### 예2
import pickle
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)


## OS

### 내 시스템의 환경 변수 값을 알고 싶을 때 - os.environ
import os
print(os.environ)
print(os.environ['PATH'])

### 디렉터리 위치 변경하기 os.chdir
#os.chdir("C:\WINDOWS")

### 디렉터리 위치 돌려받기 - os.getcwd
#os.getcwd()

### 시스템 명령어 호출하기 - os.system
print(os.system("dir"))

### 실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
f = os.popen("dir")
print(f.read())

### shutil
import shutil
# shutil.copy("src.txt", "dst.txt")

## glob

### 디렉터리에 있는 파일들ㅇ르 리스트로 만들기 - glob(pathname)
import glob
# glob.glob("c:/doit/mark*")


## tempfile
import tempfile
filename = tempfile.mkstemp()
print(filename)

import tempfile
f = tempfile.TemporaryFile()
f.close()


## time

### time.time
import time
print(time.time())

### time.localtime
print(time.localtime(time.time()))

### time.asctime
print(time.asctime(time.localtime(time.time())))

### time.ctime
print(time.ctime())

### time.strftime
time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))

import time
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))

### time.sleep
import time
for i in range(10):
    print(i)
    time.sleep(1)


## calendar

### calendar.calendar
import calendar
print(calendar.calendar(2015))

### calendar.prcal
print(calendar.prcal(2015))
print(calendar.prmonth(2015, 12))

### calendar.weekday
print(calendar.weekday(2015, 12, 31))

### calendar.monthrange
print(calendar.monthrange(2015, 12))


## random

### 예1
import random
print(random.random())
print(random.randint(1, 10))
print(random.randint(1, 55))

### 예2
import random
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: print(random_pop(data))

### 예3
def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

### 예4
import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)


## webbrowser
import webbrowser
webbrowser.open("https://google.com")
webbrowser.open_new("https://google.com")


### 점프 투 파이썬 - 스레드를 다루는 threading 모듈

#### 예1
import time

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working%s\n" % i)
print("Start")

for i in range(5):
    long_task()
print("End")

#### 예2
import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working%s\n" % i)
print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("End")