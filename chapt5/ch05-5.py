# 내장 함수

## abs
print(abs(3))
print(abs(-3))
print(abs(-1.2))


## all
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))


## any
print(any([1, 2, 3, 0]))
print(any([0, ""]))


## chr
print(chr(97))
print(chr(48))


## dir
print(dir([1, 2, 3]))
print(dir({'1':'a'}))


## divmod
print(divmod(7, 3))


## enumerate
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)


## eval
print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))


## filter

### 사용 x
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1, -3, 2, 0, -5, 6]))

### 사용 o - 1
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

### 사용 o - 2
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))


## hex
print(hex(234))
print(hex(3))


## id
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))
print(id(4))


## input
a = input()
print(a)
b = input("Enter: ")
print(b)


## int
print(int('3'))
print(int(3.4))
print(int('11', 2))
print(int('1A', 16))


## isinstance
class Person: pass

a = Person()
print(isinstance(a, Person))

b = 3
print(isinstance(b, Person))


## len
print(len("python"))
print(len([1, 2, 3]))
print(len([1, 'a']))


## list
print(list("python"))
print(list((1, 2, 3)))
a = [1, 2, 3]
b = list(a)
print(b)


## map

### 사용 x
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

### 사용 o - 1
def two_times(x): return x*2
print(list(map(two_times, [1, 2, 3, 4])))

### 사용 o - 2
print(list(map(lambda a: a*2, [1, 2, 3, 4])))


## max
print(max([1, 2, 3]))
print(max("python"))


## min
print(min([1, 2, 3]))
print(min("python"))


## oct
print(oct(34))
print(oct(12345))


## open
f = open("binary_file", "rb")

fread = open("read_mode.txt", 'r')
fread2 = open("read_mode.txt")

fappend = open("append_mode.txt", 'a')


## ord
print(ord('a'))
print(ord('0'))


## pow
print(pow(2, 4))
print(pow(3, 3))


## range

### 인수가 하나일 경우
print(list(range(5)))

### 인수가 2개일 경우
print(list(range(5, 10)))

### 인수가 3개일 경우
print(list(range(1, 10, 2)))
print(list(range(0, -10, -1)))


## round
print(round(4.6))
print(round(4.2))
print(round(5.678, 2))


##sorted
print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))
print(sorted("zero"))
print(sorted((3, 2, 1)))


## str
print(str(3))
print(str('hi'))
print(str('hi'.upper()))


## sum
print(sum([1, 2, 3]))
print(sum((4, 5, 6)))


## tuple
print(tuple("abc"))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))


## type
print(type("abc"))
print(type([]))
print(type(open("test", 'w')))


## zip
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))
