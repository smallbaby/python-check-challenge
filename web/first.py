# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/7/22 
# Desc:
from Werkzeug import *

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, ssss!</h1>'