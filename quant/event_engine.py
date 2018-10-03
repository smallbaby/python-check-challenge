# -*- coding: utf-8 -*-
# Author: kai.zhang01


from collections import defaultdict
from queue import Queue, Empty
from threading import Thread


class Event:
    def __init__(self, event_type, data=None):
        self.event_type = event_type
        self.data =data

class EventEngine:
    def __init__(self):
        self.__queue = Queue()
        self.__active = True
        self.__thread = Thread(target=self.__run, name='EventEngine.__thread')
        self.__handlers = defaultdict(list)

    def __run(self):
        # 启动
        while self.__active:
            try:
                event = self.__queue.get(block=True, timeout=1)
                handle_thread = Thread(target=self.__process, name='_process')
                handle_thread.start()
            except:
                pass

    def __process(self, event):
        if event.event_type in self.__handlers:
            for handler in self.__handlers[event.event_type]:
                handler(event)

    def start(self):
        self.__active = True
        self.__thread.start()

    def stop(self):
        self.__active = False
        self.__thread.join()

    def register(self, event_type, handler):
        if handler not in self.__handlers[event_type]:
            self.__handlers[event_type].append(handler)

    def unregister(self, event_type, handler):
        handler_list = self.__handlers[event_type]
        if handler_list is None:
            return
        if handler in handler_list:
            handler_list.remove(handler)

        if len(handler_list) == 0:
            self.__handlers.pop(event_type)
    def put(self, event):
        self.__queue.put(event)

    def queue_size(self):
        return self.__queue.qsize()











