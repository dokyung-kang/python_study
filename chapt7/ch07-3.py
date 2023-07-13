# 메타 주스
import re

## |
p = re.compile('Crow|Servo')
m = p.match('CrowHello')
print(m)


## ^
print(re.search('^Life', 'Life is too short'))
print(re.search('^Life', 'My Life'))


## $
print(re.search('short$', 'Life is too short'))
print(re.search('short$', 'Life is too short, you need python'))


## \A
### 문자열의 처음과 매치


## \Z
### 문자열의 끝과 매치


## \b
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))


## \B
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
print('the declassified algorithm')
print(p.search('one subclass is'))



# 그루핑

## 예1 - ()
p = re.compile('(ABC)+')
m = p.search('ABCABCABC OK?')
print(m)
print(m.group(0))


## 예2
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))


## 예3
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))


## 예4
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3))


## 그루핑된 문자열 재참조하기
p = re.compile(r'(\b\w+)\s+\1')
m = p.search('Paris in the the spring').group()
print(m)



# 그루핑된 문자열에 이름 붙이기

## 예
## (?P<name>\w)\s+((\d+)[-]\d+[-]\d+)

## 예1
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))


## 예2
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
m = p.search('Paris in the the spring').group()
print(m)



# 전방 탐색
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

## 긍정적 전방 탐색
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

### .*[.].*$

### .*[.][^b].*$

### .*[.]([^b]..|.[^a].|..[^t])$

### .*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$


## 부정형 전방 탐색

### .*[.](?!bat$).*$

### .*[.](?!bat$|exe$).*$



# 문자열 바꾸기

## 예1
p = re.compile('(blue|white|red)')
m = p.sub('colour', 'blue socks and red shoes')
print(m)


### 예2
m = p.sub('colour', 'blue socks and red shoes', count=1)
print(m)


### 점프 투 파이썬 - sub 메서드와 유사한 subn 메서드


## sub 메서드를 사용할 때 참조 구문 사용하기
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-2134-1234"))

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<2> \g<1>", "park 010-2134-1234"))


## sub 메서드의 매개변수로 함수 넣기
def hexrepl(match):
    value = int(match.group())
    return hex(value)
p = re.compile(r'\d+')
m = p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
print(m)



# Greedy vs Non-Greedy

## 예1
s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group())


## 예2
print(re.match('<.*?>', s).group())