# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/10 
# Desc:  测试参数模块

import argparse

parser = argparse.ArgumentParser()

# type=int  类型
# choices=[0, 1, 2] 可选项
# default=2  默认值

parser.add_argument("-v", "--verbosity", help="increase output verbosity")
args = parser.parse_args()

if args.verbosity:
    print('pass')


