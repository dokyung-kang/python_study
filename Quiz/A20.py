# 정답

import re

num = re.compile(".*[@].*[.](?=com$|net$).*$")

print(num.match("pahkey@gmail.com"))
print(num.match("dkin@daum.net"))
print(num.match("lee@myhome.co.kr"))
