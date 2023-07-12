# 하위 디렉터리 검색하기


#1
# def search(dirname):
#     print(dirname)
#
# search("C:/")

#2
# import os
#
# def search(dirname):
#     filenames = os.listdir(dirname)
#     for filename in filenames:
#         full_filename = os.path.join(dirname, filename)
#     print(full_filename)
#
# search("C:/")

#3
# import os
#
# def search(dirname):
#     filenames = os.listdir(dirname)
#     for filename in filenames:
#         full_filename = os.path.join(dirname, filename)
#         ext = os.path.splitext(full_filename)[-1]
#         if ext == ".py":
#             print(full_filename)
#
# search("C:/")

#4
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == ".py":
                    print(full_filename)
    except PermissionError:
        pass

search("c:/")


### 점프 투 파이썬 - 하위 디렉터리 검색을 쉽게 해주는 os.walk
import os
for (path, dir, files) in os.walk("C:/"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))
