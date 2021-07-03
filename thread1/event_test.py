# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/9/6 
# Desc:

from queue import Queue, Empty
from threading import *


class EventManager:
    def __init__(self):
        # 事件管理器
        self.__eventQueue = Queue()
        # 开关
        self.__active = False
        # handler
        self.__thread = Thread(target=self.__Run)
        self.__handlers = {}

    def __Run(self):
        while self.__active == True:
            try:
                event = self.__eventQueue.get(block=True, timeout=1)
                self.__EventProcess(event)
            except:
                pass

    def __EventProcess(self, event):
        if event.type_ in self.__handlers:
            for hander in self.__handlers[event.type_]:
                hander(event)

    def Start(self):
        self.__active = True
        self.__thread.start()

    def Stop(self):
        self.__active = False
        self.__thread.join()

    def AddEventListener(self, type_, handler):
        """绑定事件与监听器"""
        try:
            handlerList = self.__handlers[type_]
        except KeyError:
            handlerList = []

        self.__handlers[type_] = handlerList

        if handler not in handlerList:
            handlerList.append(handler)

    def SendEvent(self, event):
        self.__eventQueue.put(event)

class Event:
    def __init__(self, type_=None):
        self.type = type_
        self.dict = {}


EVENT_ARTICAL = "Event_Artical"

# 事件源
class PublicAccounts:
    def __init__(self, eventManager):
        self.__eventManager = eventManager

    def WriteNewArtical(self):
        event = Event(type_=EVENT_ARTICAL)

        event.dict['artical'] = u'hello'
        # send
        self.__eventManager.SendEvent(event)
        print('send new actilc')


class Listener:
    def __init__(self, name):
        self.__name = name

    def ReadArtical(self, event):
        print('%s receive a new book' % self.__name)
        print('正在阅读新文章:%s' % event.dict['artical'])

def test():
    listener1 = Listener('u1')
    listener2 = Listener('u2')

    eventManager = EventManager()

    # 绑定

    eventManager.AddEventListener(EVENT_ARTICAL, listener1.ReadArtical)
    eventManager.AddEventListener(EVENT_ARTICAL, listener2.ReadArtical)
    eventManager.Start()

    publicAcc = PublicAccounts(eventManager)

    timer = Timer(2, publicAcc.WriteNewArtical)
    timer.start()

if __name__ == '__main__':
    test()


















