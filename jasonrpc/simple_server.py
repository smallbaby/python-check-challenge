# -*- coding: utf-8 -*-
# Author: kaizhang01

import grpc
import hello_pb2
import hello_pb2_grpc
import time

_ONE_DAY_IN_SECONDS = 60 * 60

from concurrent import futures


class sayHello(hello_pb2_grpc.ServerServicer):
    def sayHello(self, request, context):
        if request.case_id == 1:
            print('818全链路压测...')
        else:
            print('普通压测...')
        return hello_pb2.Msg(message="hello~~~~~~")


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=30))
    hello_pb2_grpc.add_ServerServicer_to_server(sayHello(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('server start.....')
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
