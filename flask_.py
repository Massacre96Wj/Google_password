# -*- coding: utf-8 -*-
from flask import Flask, request
import time
import json

app = Flask(__name__)


@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        _txtName = '%s_%s.txt' % (request.remote_addr,
                                  time.strftime('%Y%m%d%H%M%S', time.localtime()))
        with open(_txtName, 'w', encoding='utf-8') as f:
            f.writelines(json.loads(request.data))
    return "小哥，里面玩儿啊"


if __name__ == '__main__':
    # 端口可自行设置
    app.run(host='192.168.64.1', port=9999)