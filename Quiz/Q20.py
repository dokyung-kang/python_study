# 내가 푼 문제

import re

num = re.compile(".*[@].*[.](?=com$|net$).*$")

print(num.match("naver@naver.com"))
print(num.match("daum@daum.net"))
print(num.match("temp@temp.t"))
