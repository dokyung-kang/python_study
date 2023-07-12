# 간단한 메모장 만들기


#1
# import sys
#
# option = sys.argv[1]
# memo = sys.argv[2]
#
# print(option)
# print(memo)

#2
# import sys
#
# option = sys.argv[1]
#
# if option == '-a':
#     memo = sys.argv[2]
#     f = open('memo.txt', 'a')
#     f.write(memo)
#     f.write('\n')
#     f.close()

#3
import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)