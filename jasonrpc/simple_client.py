# -*- coding: utf-8 -*-
# Author: kaizhang01

import grpc
import hello_pb2
import hello_pb2_grpc
from google.protobuf import struct_pb2


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = hello_pb2_grpc.ServerStub(channel)
    # 自定义struct
    struct = struct_pb2.Struct()
    struct['name'] = 'zhangkai'
    struct['age'] = 34
    response = stub.sayHello(hello_pb2.Event(case_id=1, name="压测A", actor="12913", x=struct))
    print(response)


if __name__ == '__main__':
    run()
