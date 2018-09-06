# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/9/5 
# Desc:
import os
import sys
import logbook
from logbook import Logger, StreamHandler, FileHandler

logbook.set_datetime_format('local')


class DefaultHandler(object):
    """ lOG 类 """
    def __init__(self, name ='default', log_type='stdout', filepath='default.log', loglevel='DEBUG'):
        """

        :param name:
        :param log_type:stdout 输出到屏幕  file 输出到文件
        :param filepath:
        :param loglevel:设定log等级 ['CRITICAL', 'ERROR', 'WARNING', 'NOTICE', 'INFO', 'DEBUG', 'TRACE', 'NOTSET']
        """
        self.log = Logger(name)
        if log_type == 'stdout':
            StreamHandler(sys.stdout, level=loglevel).push_application()
        elif log_type == 'file':
            if os.path.isdir(filepath) and not os.path.exists(filepath):
                os.makedirs(os.path.dirname(filepath))
            file_hander = FileHandler(filepath, level=loglevel)
            self.log.handlers.append(file_hander)

    def __getattr__(self, item, *args, **kwargs):
        return self.log.__getattribute__(item, *args, *kwargs)