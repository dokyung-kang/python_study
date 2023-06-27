# 문자열은 어떻게 만들고 사용할까?

## 큰따옴표(")로 양쪽 둘러싸기
a = "Hello World"


## 작은 따옴표(')로 양쪽 둘러싸기
a = 'Python is fun'


## 큰 따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
a = """
Life is too short, You need python
"""


## 작은따옴표 3개를 연곡(''')으로 써서 양쪽 둘러싸기
a = '''
Life is too short, You need python
'''



# 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶은 대

## 문자열에 작은따옴표(') 포함시키기
food = "Python's favorite food is perl"
print(food)


## 문자열에 큰따옴표(") 포함시키기
say = '"Python is very easy." he says'
print(say)


## 백슬레시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
food = "Python\'s favorite food is perl"
say = '\"Python is very easy.\" he says'
print(food)
print(say)



# 여러 줄인 문자열을 변수에 대입하고 싶을 때

## 줄을 바꾸는 이스케이프 코드 '\n' 삽입하기
multiline = "Life is too short\nYou need python"
print(multiline)


## 연속되는 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 사용하기

### 작은따옴표 3개를 사용한 경우
multiline = '''
Life is too short
You need python
'''
print(multiline)

### 큰따옴표 3개를 사용한 경우
multiline = """
Life is too short
You need python
"""
print(multiline)



# 문자열 연산하기

## 문자열 더해서 연결하기 (Concatenation)
head = "Python"
tail = " is fun!"
print(head + tail)


## 문자열 곱하기
a = "python"
print(a * 2)


## 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)


## 문자열 길이 구하기
a = "Life is too short"
b = len(a)
print(b)



# 문자열 인덱싱과 슬라이싱

## 문자열 인덱싱

### 예1
a = "Life is too short, Ypu need Python"
print(a[3])         # 문자열을 네번째 문자

### 예2
a = "Life is too short, Ypu need Python"
print(a[0])         
print(a[12])
print(a[-1])        # 뒤에서부터 세어 첫 번째가 되는 문자, 가장 마지막 문자

### 예3
a = "Life is too short, Ypu need Python"
print(a[-2])        # 뒤에서 두 번째 문자
print(a[-5])        # 뒤에서 다섯 번째 문자


## 문자열을 슬라이싱하는 방법

### 예1
a = "Life is too short, Ypu need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

### 예2
a = "Life is too short, Ypu need Python"
b = a[0:4]
print(b)

### 예3
a = "Life is too short, Ypu need Python"
b = a[0:3]          # 0 <= a < 3
print(b)

### 예4 - 공백 포함 가능
a = "Life is too short, Ypu need Python"
b = a[0:5]
print(b)

### 예5 - 시작 번호 0일 필요 없음
a = "Life is too short, Ypu need Python"
b = a[0:2]
c = a[5:7]
d = a[12:17]
print(b)
print(c)
print(d)

### 예6 - 끝 번호 생략하면 문자열의 끝까지
a = "Life is too short, Ypu need Python"
b = a[19:]
print(b)

### 예7 - 시작 번호 생략하면 문자열 처음부터
a = "Life is too short, Ypu need Python"
b = a[:17]
print(b)

### 예8 - 시작 번호, 끝 번호 생략하면 문자열의 처음부터 끝까지
a = "Life is too short, Ypu need Python"
b = a[:]
print(b)

### 예9 - 마이노스(-) 기호 사용 가능
a = "Life is too short, Ypu need Python"
b = a[19:-7]
print(b)


## 슬라이싱으로 문자열 나누기

### 예1
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

### 예2
a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)



# 문자열 포매팅

## 문자열 포매팅 따라 하기

### 숫자 바로 대입
a = "I eat %d apples." % 3
print(a)

### 문자열 바로 대입
a = "I eat %s apples." % "five"
print(a)

### 숫자 값을 나타내는 변수로 대입
number = 3
a = "I eat %d apples." % number
print(a)

### 2개 이상의 값 넣기
number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)


## 문자열 포맷 코드

### 예1 - %s는 어떤 값이든 변환 가능
a = "I have %s apples" % 3
print(a)
a = "rate is %s" % 3.234
print(a)

### 예2
a = "Error is %d%%." % 98
print(a)


## 포맷 코드와 숫자 함께 넣기

### 정렬과 공백
a = "%10s" % "hi"
print(a)

### 정렬과 공백 반대
a = "%-10sjane" % "hi"
print(a)

### 소수점 표현하기
a = "%0.4f" % 3.42134234
print(a)
a = "%10.4f" % 3.42134234
print(a)


## 포맷 함수를 사용하여 포맷팅

### 숫자 바로 대입하기
a = "I eat {0} apples".format(3)
print(a)

### 문자열 바로 대입하기
a = "I eat {0} apples".format("five")
print(a)

### 숫자 값을 가진 변수로 대입하기
number = 3
a = "I eat {0} apples.".format(number)
print(a)

### 2개 이상의 값 넣기
number = 10
day = "three"
a = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(a)

### 이름으로 넣기
a = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(a)

### 인덱스와 이름ㅇ르 혼용해서 넣기
a = "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
print(a)

### 왼쪽 정렬
a = "{0:<10}".format("hi")
print(a)

### 오른쪽 정렬
a = "{0:>10}".format("hi")
print(a)

### 가운데 정렬
a = "{0:^10}".format("hi")
print(a)

### 공백 채우기
a = "{0:^10}".format("hi")
print(a)
b = "{0:!<10}".format("hi")
print(a)
print(b)

### 소수점 표현하기
y = 3.42134234
z = "{0:10.5f}".format(y)
print(z)

### {또는} 문자 표현하기
a = "{{ and }}".format()
print(a)


## f문자열 포매팅

### 예1
name = '홍길동'
age = 30
a = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(a)

### 예2 - 변수값 생성 후 그 값을 참조가능
age = 30
a = f'나는 내년이면 {age + 2}살이 된다.'
print(a)

### 예3 - 딕셔너리 사용
d = {'name':'홍길동', 'age':30}
a = f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
print(a)

### 예4 - 정렬
a = f'{"hi":<10}'
b = f'{"hi":>10}'
c = f'{"hi":^10}'
print(a)
print(b)
print(c)

### 예5 - 공백 채우기
a = f'{"hi":=^10}'
b = f'{"hi":!<10}'
print(a)
print(b)

### 예6 - 소수점
y = 3.42134234
a = f'{y:0.4f}'
b = f'{y:10.4f}'
print(a)
print(b)

### 예7 - f문자열에서 {}문자 표시
a = f'{{ and }}'
print(a)



# 문자열 관련 함수

## 문자 개수 세기(count)
a = "hobby"
c = a.count('b')
print(c)


## 위치 알려주기 1 (find)
a = "Python is the best choice"
c = a.find('b')
d = a.find('k')
print(c)
print(d)


## 위치 알려주기 2 (index)
a = "Life is too short"
b = a.index('t')
print(b)
"""
c = a.index('k')
print(c)
"""         # 해당되는거 없으면 에러남

## 문자열 삽입(join)
a = ",".join('abcd')
print(a)
b = ",".join(['a', 'b', 'c', 'd'])
print(b)


## 소문자를 대문자로 바꾸기 (upper)
a = "hi"
b = a.upper()
print(b)


## 대문자를 소문자로 바꾸기 (lower)
a = "HI"
b = a.lower()
print(b)


## 왼쪽 공백 지우기 (lstrip)
a = " hi "
b = a.lstrip()
print(b)


## 오른쪽 공백 지우기 (rstrip)
a = " hi "
b = a.rstrip()
print(b)


## 양쪽 공백 지우기 (strip)
a = " hi "
b = a.strip()
print(b)


## 문자열 바꾸기 (replac)
a = "Life is too short"
b = a.replace("Life", "Your leg")
print(b)


## 문자열 나눈기 (split)
a = "Life is too short"
a1 = a.split()
print(a1)
b = "a:b:c:d"
b1 = b.split(':')
print(b1)