# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/24 
# Desc:

import tornado.web
import datetime
import collections
from asyncio import wrap_future
from tornado.options import options
import tornado.ioloop
from tornado.concurrent import futures
from tornado_test.handler.service import fetch_huobi_price


class AwaitableThreadPoolExecutor(futures.ThreadPoolExecutor):
    def submit(self, *args, **kwargs):
        return wrap_future(super().submit(*args, **kwargs))

    def map(self, *args, **kwargs):
        for future in super().map(*args, **kwargs):
            yield wrap_future(future)


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.thread_pool = AwaitableThreadPoolExecutor()

    def write_error(self, status_code, **kwargs):
        msg = kwargs.pop('message', '')
        self.set_status(300, msg)
        self.finish({
            'status_code': status_code,
            'message': msg
        })

class HelloHandler(BaseHandler):
    async def get(self, *args, **kwargs):
        start = self.get_query_argument('start', None)
        if not start:
            return self.write_error(400, message = 'Missing required args:start')
        end = self.get_argument('end', None)
        try:
            start_timestamp = int(start) if len(start) == 10 else int(start) / 10
            start_time = datetime.datetime.utcfromtimestamp(start_timestamp)
            if end:
                end_timestamp = int(end) if len(end) == 10 else int(end) / 10
                end_time = datetime.datetime.utcfromtimestamp(end_timestamp)
        except(TypeError, ValueError, OverflowError):
            return self.write_error(400, message='Invalid argument: start or end')

        result = collections.defaultdict(dict)

        async for item in fetch_huobi_price(start_time, end_time):
            pass
            ## 数据处理


class Application(tornado.web.Application):
    def __init__(self):
        urls =[
            ('/', HelloHandler)
        ]

        settings = dict(debug=True)

def main(port, host =''):
    print('start listen port is {}'.format(port))
    options.parse_command_line()
    Application().listen(port)
    tornado.ioloop.IOLoop.instance().start()