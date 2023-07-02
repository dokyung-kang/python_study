# 패키지 만들기
def render_test():
    print("render")



# relative 패키지

## 예1
from game.sound.echo import echo_test
def render_test():
    print("render")
    echo_test


## 예2
from ..sound.echo import echo_test

def render_test():
    print("render")
    echo_test()