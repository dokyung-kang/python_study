# 연습 문제

## Q1.
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
print(is_odd(3))
print(is_odd(4))


## Q2.
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

avg_numbers(1, 2)
avg_numbers(1, 2, 3, 4, 5)


## Q3.
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s입니다." % total)


## Q4.
### 3


## Q5.
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()


## Q6.
user_input = input("저장할 내용을 입력하세요: ")
f = open('test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close()


## Q7.
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()