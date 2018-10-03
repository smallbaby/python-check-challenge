# -*- coding: utf-8 -*-
# Author: https://github.com/smallbaby/easyquant/blob/master/easyquant/main_engine.py

import importlib
import os
import pathlib
import signal
import sys
import threading
import time
from collections import OrderedDict
from threading import Thread, Lock

from logbook import Logger, StreamHandler

from quant.event_engine import EventEngine

log = Logger(os.path.basename(__file__))
StreamHandler(sys.stdout).push_application()


class MainEngine:
    # 猪引擎
    def __init__(self, broker=None, need_data=None, quotation_engines=None
                 ,tzinfo=None):
        self.broker = broker

        #  账户检测、设置
        #####
        self.event_engine = EventEngine()
        self.strategies = OrderedDict()
        self.strategy_list = list()
        self.is_watch_strategy = False # 动态加载策略
        self._cache = {}
        self._modules = {}
        self._names = None
        self.lock = Lock()
        self._watch_thread = Thread(target=self._load_strategy, name='xxxx')

        self.before_shutdown = []
        self.main_shutdown = []
        self.after_shutdown = []

        print('启动主引擎')

    def start(self):
        self.event_engine.start()
        self._add_main_


    def load(self, names, strategy_file):
        with self.lock:
            mtime = os.path.getatime(os.path.join('strategies', strategy_file))

            reload = False

            strategy_module_name = os.path.basename(strategy_file)[:-3]
            new_module = lambda strategy_module_name: importlib.import_module('.' + strategy_module_name, 'strategies')
            strategy_module = self._modules.get(strategy_file, new_module(strategy_module_name))
            if self._cache.get(strategy_file, None) == mtime:
                return
            elif self._cache.get(strategy_file, None) is not None:
                pass





















