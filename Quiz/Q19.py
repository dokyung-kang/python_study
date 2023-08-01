# 내가 푼 문제

import re

phone = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

change = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = change.sub("\g<1>-####", phone)

print(result)