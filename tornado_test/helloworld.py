# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/23 
# Desc:

import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options

tornado.options.define('port', default=8000, type=int, help='run server on the given port')
tornado.options.define('test', default=[], type=str, multiple=True, help='test')



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello,world')




if __name__ == '__main__':
    application = tornado.web.Application([
        (r'/', MainHandler)
    ])
    tornado.options.parse_command_line() # 参数、支持config文件形式
    print(tornado.options.options.port)
    http_server = tornado.httpserver.HTTPServer(application)
    # application.listen(8888)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()
    #tornado.ioloop.IOLoop.instance().start()