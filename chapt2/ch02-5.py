# 딕셔너리는 어떻게 만들까?

## 기본 모습
dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}

### 예1 - Key 정수, Value - 문자열
a = {1: 'hi'}

### 예2 - Value 리스트
a = {'a': [1, 2, 3]}



# 딕셔너리 쌍 추가, 삭제하기

## 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pay'
print(a)

a[3] = [1, 2, 3]
print(a)


## 딕셔너리 요소 삭제하기
del a[1]
print(a)



# 딕셔너리를 사용하는 방법

## 딕셔너리에서 Key 사용해 Value 얻기
grade = {'pay': 10, 'julliet': 99}
print(grade['pay'])
print(grade['julliet'])

a = {1: 'a', 2: 'b'}
print(a[1])
print(a[2])

a = {'a':1, 'b':2}
print(a['a'])
print(a['b'])

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])


## 딕셔너리 만들 때 주의할 사항 - 중복 무시
a = {1:'a', 1:'b'}
print(a)



# 딕셔너리 관련 함수

## Key 리스트 만들기 (Keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())

for k in a.keys():
    print(k)

b = list(a.keys())
print(b)


## Value 리스트 만들기(values)
print(a.values())


## Key, Value 쌍 얻기(items)
b = a.items()
print(b)


## Key: Value 쌍 모두 지우기(clear)
a.clear()
print(a)


## Key로 Value 얻기 (get)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
b = a.get('name')
print(b)
c = a.get('phone')
print(c)

### 예1 - 값 없을 시 디폴트 값 설정
b = a.get('foo', 'bar')
print(b)


## 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a1 = 'name' in a
print(a1)
a2 = 'email' in a
print(a2)

# 나 혼자 코딩!
## 다음 표를 딕셔너리로 만드시오
### 항목      값
### name    홍길동
### birth   1128
### age     30
dic = {'name': '홍길동', 'birth': '1128', 'age': '30'}