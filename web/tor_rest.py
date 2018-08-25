# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/25 
# Desc:
import os
import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, Select\n')

    def post(self):
        self.write('hello, Add\n')

    def put(self):
        self.write('hello, Update\n')

    def delete(self):
        self.write('hello, Delete\n')


if __name__ == '__main__':
    settings = {
        'debug': True,
        'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        'templete_path': os.path.join(os.path.dirname(__file__), 'template'),
    }

    application = tornado.web.Application([
        (r'/', MainHandler),
    ], **settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

"""
测试：
curl -X DELETE 'localhost:8888'
curl 'localhost:8888'
curl -X PUT 'localhost:8888'
curl -d post 'localhost:8888'

"""