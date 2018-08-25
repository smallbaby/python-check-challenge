# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/25 
# Desc:


class GreekGetter(object):
    def __init__(self):
        self.trans = dict(dog='aaaa', cat='eeeee')

    def get(self, msgid):
        return self.trans.get(msgid, str(msgid))


class EnglishGetter(object):
    def get(self, msgid):
        return str(msgid)


def get_localizer(language='English'):
    languages = dict(English=EnglishGetter, Greek=GreekGetter)
    return languages[language]


if __name__ == '__main__':
    e, g = get_localizer(language='English'), get_localizer(language='Greek')
    for msgid in 'dog parrot cat bear'.split():
        print(e.get(msgid))
        print(g.get(msgid))
