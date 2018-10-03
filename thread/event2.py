# -*- coding: utf-8 -*-

from queue import Queue, Empty
from threading import *
from collections import defaultdict

class Event(object):
    """事件"""
    def __init__(self, type_, data=None):
        self.event_type = type_
        self.data = data
        self.dict = {}

### 事件驱动引擎
class EventEngine:
    def __init__(self):
        self.__queue = Queue() # 事件队列
        self.__active = True # 事件开关
        self.__thread = Thread(target=self.__run, name='event engine run thread')
        self.__handlers = defaultdict(list)

    def __run(self):
        # 启动引擎
        while self.__active:
            try:
                event = self.__queue.get(block=True, timeout=1)
                handler_thread = Thread(target=self.__proccess, name='eventEngine_process', args=(event,))
                handler_thread.start()
            except:
                pass

    def _start(self):
        self.__active = True
        self.__run()

    def __stop(self):
        self.__active = False
        self.__thread.join()


    def send(self, event):
        self.__queue.put(event)

    def size(self):
        return self.__queue.qsize()

    def __proccess(self, event):
        # 事件处理
        print('__pro:', event)
        if event.event_type in self.__handlers:
            print(event)
            for handler in self.__handlers[event.event_type]:
                handler(event)


    def addHandler(self, type_, handler):
        if handler not in self.__handlers[type_]:
            self.__handlers[type_].append(handler)
        print(self.__handlers)

EVENT_TYPE_DATA = 'data'
class KLineEvent:
    def __init__(self, EventEngine):
        self.__event_engine = EventEngine

    def check(self):
        print('_check, start')
        event = Event(EVENT_TYPE_DATA)
        event.data = 'helloworld'
        self.__event_engine.send(event)
        print('send succ...')

class Strategy:
    def __init__(self, name):
        self.__name = name

    def handler(self, event):
        print(event.data)

def test():
    s1 = Strategy('s1')
    s2 = Strategy('s2')
    eventEngine = EventEngine()
    eventEngine.addHandler(EVENT_TYPE_DATA, s1.handler)
    eventEngine.addHandler(EVENT_TYPE_DATA, s2.handler)
    eventEngine._start()
    kline = KLineEvent(eventEngine).check()

    # timer = Timer(1, kline.check)
    # timer.start()

if __name__ == '__main__':
    test()



