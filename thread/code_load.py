# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/9/8 
# Desc:

import codecs
import copy
from six import exec_

class CodeLoader:
    def __init__(self, strategyfile):
        self._strategyfile = strategyfile

    def compile_strategy(self, source_code, strategyfile, scope):
        code = compile(source_code, strategyfile, 'exec')
        exec_(code, scope)
        return scope
    #
    def load(self, scope):
        with codecs.open(self._strategyfile, encoding="utf-8") as h:
            source_code = h.read()
        source_code = 'from api import *\n' + source_code
        return self.compile_strategy(source_code, self._strategyfile, scope)