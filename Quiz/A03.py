# 정답

a = [1, 2, 3]
print(id(a))
a = a + [4, 5]
print(a)
print(id(a))
# a의 값이 변하는 것이 아니라 두 리스트가 더해진 새로운 리스트를 반환

a = [1, 2, 3]
print(id(a))
a.extend([4, 5])
print(a)
print(id(a))
# 주소 값이 변하지 않고 그대로 유지
