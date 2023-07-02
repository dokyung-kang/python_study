# if __name__ == "__main__"의 의미

## 예1 - if __name__ == "__main__" 없음
def add(a, b):
    return a + b
def sub(a, b):
    return a - b

print(add(1, 4))
print(sub(4, 2))


## 예2 - if __name__ == "__main__" 있음
def add(a, b):
    return a + b
def sub(a, b):
    return a - b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))