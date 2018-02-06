﻿from flask import Flask

app = Flask(__name__)


# 데코레이터 없이 함수를 선언하고
def index():
    return 'hello'

app.add_url_rule('/index', 'endpoint!!', index)
# add_url_rule이라는 함수로 리소스를 추가한다
# rule, endpoint, view_func 순서

# route 데코레이터 안에서도 self.add_url_rule로 엔드포인트에 view function을 할당한다
# https://github.com/pallets/flask/blob/master/flask/app.py#L1212

app.run()
