# 정답

user_input = input("구구단을 출력할 숫자를 입력하세요(2~9):")
dan = int(user_input)
for i in range(1, 10):
    print(i*dan, end=' ')
    