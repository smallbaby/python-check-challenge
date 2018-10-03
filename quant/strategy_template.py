# -*- coding: utf-8 -*-
# Author: kai.zhang01

import sys
import traceback


class StrategyTemplate:
    name = 'defaultST'

    def __init__(self, user, log_handler, main_engine):
        self.user = user
        self.main_engine = main_engine
        self.clock_engine = main_engine.clock_engine
        self.log = self.log_handler() or log_handler
        self.init()

    def init(self):
        pass

    def strategy(self, event):
        pass

    def run(self, event):
        try:
            self.strategy(event)
        except:
            exc_type, exc_value, exc_trackback = sys.exc_info()
            self.log.error('')

    def clock(self, event):
        pass


    def log_handler(self):
        return None

    def shutdown(self):
        pass




