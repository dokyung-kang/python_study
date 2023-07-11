# 구구단 프로그램 2단

#1
# result = GuGu(2)

#3
# def GuGu(n):
#     print(i)

#4
# def GuGu(n):
#     result = []

#5
# def GuGu(n):
#     result = []
#     result.append(n*1)
#     result.append(n*2)
#     result.append(n*3)
#     result.append(n*4)
#     result.append(n*5)
#     result.append(n*5)
#     result.append(n*6)
#     result.append(n*7)
#     result.append(n*8)
#     result.append(n*9)
#     return result
# print(GuGu(2))

#6
# i = 1
# while i < 10:
#     print(i)
#     i = i + 1

#7
def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result

print(GuGu(2))