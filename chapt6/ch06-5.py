# 탭을 4개의 공백으로 바꾸기

#1
# import sys
#
# src = sys.argv[1]
# dst = sys.argv[2]
#
# print(src)
# print(dst)

#2
# import sys
#
# src = sys.argv[1]
# dst = sys.argv[2]
#
# print(src)
# print(dst)
#
#
# f = open(src)
# tab_content = f.read()
# f.close()
#
# space_content = tab_content.replace("\t", " "*4)
# print(space_content)

#3
import sys

src = sys.argv[1]
dst = sys.argv[2]

print(src)
print(dst)


f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)
print(space_content)


f = open(dst, 'w')
f.write(space_content)
f.close()