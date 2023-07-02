# 패키지 만들기

## 패키지 안의 함수 실행하기

### echo 모듈 import
import game.sound.echo
game.sound.echo.echo_test()

### echo 모듈 있는 디렉터리까지 from ... import
from game.sound import echo
echo.echo_test()

### echo 모듈의 echo_test 함수를 직접 import
from game.sound.echo import echo_test
echo_test()



# __init__.py 용도
from game.sound import *
echo.echo_test()


# 나 혼자 코딩!
## *을 사용하여 render.py 파일 안의 render_test 함수를 사용해보시오.
from game.graphic import *
render.render_test()



# relative 패키지

## 예1
from game.graphic.render import render_test
render_test()


## 예2
from game.graphic.render import render_test
render_test()