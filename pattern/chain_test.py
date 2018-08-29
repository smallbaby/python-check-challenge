# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/29 
# Desc:责任链式模式

import abc


class Hander(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        res = self._hande(request)
        if not res:
            self._successor.handle(request)

    @abc.abstractmethod
    def _hande(self, request):
        raise NotImplementedError('must provide implemention in subclass')


class ConcreateHandler1(Hander):
     def _hande(self, request):
         if 0<request<=10:
             print('request{} handled in hander 1'.format(request))
             return True


class ConcreateHandler2(Hander):
    def _hande(self, request):
        if 10 < request <= 20:
            print('request{} handled in hander 2'.format(request))
            return True

class ConcreateHandler3(Hander):
    def _hande(self, request):
        if 20 < request <= 30:
            print('request{} handled in hander 3'.format(request))
            return True

class DefaultHandler(Hander):
    def _hande(self, request):
        print('end of chain ,no handler for {}'.format(request))
        return True


class Client(object):
    def __init__(self):
        self.hander = ConcreateHandler1(ConcreateHandler3(ConcreateHandler2(DefaultHandler())))

    def delegate(self, requests):
        for request in requests:
            self.hander.handle(request)


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

if __name__ == '__main__':
    client = Client()
    requests = [2,5,14,22,18,3,10,38]
    client.delegate(requests)