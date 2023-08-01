# 내가 푼 문제

import re

p = re.compile('[a-z]+')
m = p.search("5 python")
print(m.start() + m.end())

## m.start()은 2, m.end()는 8이니 결과는 10