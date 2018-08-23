# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/19 
# Desc:


class FooParent(object):
    def __init__(self):
        self.parent = 'i am a parent'
        print('Parent')

    def bar(self, msg):
        print('%s from Parent' % msg)

class FooChild(FooParent):
    def __init__(self):
        super().__init__()
        print('Child')

    def bar(self, msg):
        super().bar(msg)
        print('Child bar fun')
        print(self.parent)

if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')