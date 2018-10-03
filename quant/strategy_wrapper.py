# -*- coding: utf-8 -*-
# Author: kai.zhang01

import multiprocessing as mp
from threading import Thread

__author__ = 'helloworld'


class ProcessWrapper(object):
    def __init__(self, strategy):
        """

        :param strategy:
        """
        self.__strategy = strategy

        # 事件队列
        self.__event_queue = mp.Queue(10000)
        # time q
        self.__clock_queue = mp.Queue(10000)

        self._proc = mp.Process(target=self._process)
        self._proc.start()

    def stop(self):
        self.__event_queue.put(0)
        self.__clock_queue.put(0)
        self._proc.join()

    def on_event(self, event):
        self.__event_queue.put(event)


    def _process_event(self):
        while True:
            try:
                event = self.__event_queue.get(block=True, timeout=1)
                if event == 0:
                    break
                self.__strategy.run(event)
            except:
                pass


    def _process_clock(self):
        # time handler
        while True:
            try:
                event = self.__clock_queue.get(block=True, timeout=1)
                if event == 0:
                    break
                self.__strategy.clock(event)
            except:
                pass

    def _process(self):
        # run
        event_thread = Thread(target=self._process_event, name='ProcessWrapper.prcess_event')
        event_thread.start()
        clock_thread = Thread(target=self._process_clock, name='ProcessWrapper.click_thread')
        clock_thread.start()

        event_thread.join()
        clock_thread.join()




