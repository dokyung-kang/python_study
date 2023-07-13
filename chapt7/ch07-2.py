# 정규 표현식의 기초, 메타 문자

## 문자 클래스[]
### ex) [0-9], [a-zA-Z]


## Dot(.)
### ex) a.b, a[.]b


## 반복(*)
### ex) ca*t


## 반복(+)
### ex) ca+t


## 반복({m, n}, ?)

### 1. {m}
#### ex) ca{2}t


### 2. {m, n}
#### ex) ca{2, 5}

### 3. ?
#### ex) ab?c



# 파이썬에서 정규 표현식을 지원하는 re모듈
import re
p = re.compile('ab*')



# 정규식을 사용한 문자열 검색
import re
p = re.compile('[a-z]+')

## match
m = p.match("python")
print(m)

m = p.match("3 python")
print(m)

#p = re.compile(정규표현식)
m = p.match("조사할 문자열")
if m:
    print('Match found: ', m.group())
else:
    print('No match')

## search
m = p.search("python")
print(m)

m = p.search("3 python")
print(m)

## findall
result = p.findall("life is too short")
print(result)

## finditer
result = p.finditer("life is too short")
print(result)



# match 객체의 메소드

## 예1
import re
p = re.compile('[a-z]+')
m = p.match("python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

## 예2
m = p.search("3 python")
print(m.group())
print(m.start())
print(m.end())
print(m.span())


### 점프 투 파이썬 - 모듈 단위로 수행하기
#### 단축 전
p = re.compile('[a-z]+')
m = p.match("python")

#### 단축 후
m = re.match('[a-z]+', "python")



# 컴파일 옵션

## DOTALL, S

### 사용 x
import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

### 사용 o
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)


## IGNORECASE, I
p = re.compile('[a-z]', re.I)
print(p.match('python'))
print(p.match('Python'))
print(p.match('PYTHON'))


## MULTILINE, M

### 사용 전
import re
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

### 사용 후
import re
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))


## VERBOSE, X
charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
&[#]
(
    0[0-7]+
    | [0-9]+
    | x[0-9a-fA-F]+
)
;
""", re.VERBOSE)



# 백슬래시 문제

## \section (x)
## [ \t\n\r\f\v]ection
## \\section (o)

p = re.compile('\\section')     # 여기도 에러남

p = re.compile('\\\\section')

p = re.compile(r'\\section')