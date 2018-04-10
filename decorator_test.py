# -*- coding:utf8 -*-


def check_is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper

class Storage(object):
    @check_is_admin
    def get_food(self, username, food):
        return 'appled'

    @check_is_admin
    def put_food(self, username, food):
        return '111'

s = Storage()
#s.get_food('hello', 'apple')
#print s.get_food('admin', 'admin')




def bread(func):
    def wrapper():
        print "AAAA"
        func()
        print "BBBB"
    return wrapper
def sandwich(food="--ham--"):
    print food


import functools
import inspect
def is_admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        func_args = inspect.getcallargs(func, *args, **kargs)
        if func_args.get('username') != 'admin':
            raise Exception('ssss')
        return func(*args, **kargs)
    return wrapper


import signal
import time
def timeout(seconds, error_massge = 'Function call timed out...'):
    def decorated(func):
        def _handle_timeout(sigum, frame):
            raise Exception(error_massge)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return functools.wraps(func)(wrapper)
    return decorated

@timeout(2, 'Function slow; aborted')
def slow_function():
    time.sleep(5)

#slow_function()



import os
#from threading import Thread
from multiprocessing import Process as Thread
def get_data(num):
    print ('sum to {0} with pid {1}'.format(num,os.getpid()))

def main():
    data = [i for i in range(10)]
    threads = []
    for num in data:
        thread = Thread(target = get_data, args=(num,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    #main()
    print map(lambda x:x*x, [i for i in range(10)])


























