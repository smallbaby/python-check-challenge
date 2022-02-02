# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2021/12/06
# Desc:

"""
统计到月用户数
"""


def autobi():
    file = open('autobi')
    for line in file.readlines():
        x = line.strip()
        x = x.split("\t")
        if len(x) > 1:
            x1 = x[0][0:7]
            x2 = x[1]
            print(x1, x2)


def sirius():
    file = open('sirius')
    for line in file.readlines():
        x = line.strip()
        x = x.split("\t")
        if len(x) > 1:
            x1 = x[0][0:7]
            x2 = x[1]
            print(x1, x2)
            if len(x) > 2:
                x3 = x[2]
                print(x1, x2)
def form():
    file = open('form')
    for line in file.readlines():
        x = line.strip()
        x = x.split("\t")
        if len(x) > 1:
            x1 = x[0][0:7]
            x2 = x[1]
            x3 = x[2]
            x4 = x[3]
            x22 = x2.split(",")
            for x222 in range(0, len(x22)):
                print(x1, x22[x222])
            x33 = x3.split(",")
            for x333 in range(0, len(x33)):
                if x33[x333]:
                    print(x1, x33[x333])
            x44 = x4.split(",")
            for x444 in range(0, len(x44)):
                if x44[x444]:
                    print(x1, x44[x444])


autobi()
sirius()
form()
