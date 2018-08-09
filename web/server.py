# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/7/22 
# Desc:
from wsgiref.simple_server import make_server
from first import application

httpd = make_server('', 8000, application)

print("serving HTTP on port 8000")
httpd.serve_forever()
