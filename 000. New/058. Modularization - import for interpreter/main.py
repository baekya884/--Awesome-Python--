# 인터프리터 언어에게 import는 제어가 분기되는 시점이기도 하다
# A에서 B를 import하고 변수 x를 선언한 상황에서, B가 A의 변수 x를 참조한다면 문제가 발생한다

import b

a = 10