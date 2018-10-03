# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/9/8 
# Desc:

from queue import Queue,Empty
from threading import *
from collections import defaultdict

class Event:
    def __init__(self, event_type, data=None, dict=None):
        self.event_type = event_type
        self.data = data
        self.dict = dict

class EventEngine:
    def __init__(self):
        self.__events = Queue()
        self.__active = False
        self.__thread = Thread(target=self._run, name='eventEngine.__thread')
        self.__eventHandler = defaultdict(list)

    def send(self, event):
        print('send:', event)
        self.__events.put(event)

    def _run(self):
        while self.__active:
            try:
                event = self.__events.get(block=True, timeout=1)
                print('run:', event)
                handler_thread = Thread(target=self._process, name='EventEngine._run._handler', args=(event,))
                handler_thread.start()
            except Empty:
                pass

    def _process(self, event):
        if event.event_type in self.__eventHandler:
            for handler in self.__eventHandler[event.event_type]:
                handler(event)

    def _stop(self):
        self.__active = False
        self.__thread.join()

    def _start(self):
        self.__active = True
        self._run()

    def addHandler(self, event_type, event):
        if event_type not in self.__eventHandler:
            self.__eventHandler[event_type] = [event]
        else:
            self.__eventHandler[event_type].append(event)

EVENT_TYPE_A = 'kline'

class EventSources:
    def __init__(self, event_engine):
        self.__eventEngine = event_engine


    def hello(self):
        event = Event(event_type=EVENT_TYPE_A)
        event.data = 'hellow,rodl'
        self.__eventEngine.send(event)


class Listener:
    def __init__(self, name):
        self.name = name

    def handler(self, event):
        print(event,event.data)


def test():
    a = Listener('a')
    b = Listener('b')
    eventEngine = EventEngine()
    eventEngine.addHandler(EVENT_TYPE_A, a.handler)
    eventEngine.addHandler(EVENT_TYPE_A, b.handler)
    eventEngine._start()
    es = EventSources(eventEngine)
    timer = Timer(2, es.hello)
    timer.start()

if __name__ == '__main__':
    test()









