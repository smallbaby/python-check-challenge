# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/29 
# Desc:
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

file_path='/Users/kaizhang/python/'

coins = {
'btcusdt': 'BTCUSDT.res',
'eosusdt': 'EOSUSDT.res',
'ethusdt': 'ETHUSDT.res',
'ltcusdt': 'LTCUSDT.res'
}


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        print('handler')
        self.finish()

class FileHandler(tornado.web.RequestHandler):
    def get(self):

        coin = self.get_argument('symbol', '')
        if coin and coin in coins:

            print('i download file handler : ', coins[coin])
            # Content-Type这里我写的时候是固定的了，也可以根据实际情况传值进来
            self.set_header('Content-Type', 'application/octet-stream')
            self.set_header('Content-Disposition', 'attachment; filename=' + coins[coin])
            # 读取的模式需要根据实际情况进行修改
            with open(file_path + '/' + coins[coin], 'rb') as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    self.write(data)
            # 记得有finish哦
            self.finish()
        else:
            self.write('error')
            self.finish()


if __name__ == "__main__":
    tornado.options.parse_command_line()

    application = tornado.web.Application([
        (r"/download", FileHandler),
        (r"/hello", HelloHandler)
    ])

    application.listen(8080) # beta 8080, online 8081
    instance = tornado.ioloop.IOLoop.instance().start()
