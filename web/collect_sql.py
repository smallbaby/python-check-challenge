# -*- coding: utf-8 -*-
# Author: kaizhang01
# Date: 2019/1/9
# Desc:

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)


@app.route('/sql/<sql>')
def sql(sql):
    print(sql)
    return "SUCCESS"


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, '/home/supdev/tmp/', secure_filename(f.filename))
        f.save(upload_path)


@app.route("/limit/<int:num>")
def limit(num):
    return "limit" + str(num)


if __name__ == '__main__':
    app.run(port=9001)
