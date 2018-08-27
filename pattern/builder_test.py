# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/27 
# Desc: builder模式，解决对象构造函数参数太多场景


def construct_building(builder):
    builder.new_building()
    builder.build_floor()
    builder.build_size()


class Building(object):
    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor:{0.floor} | Size:{0.size}'.format(self)


class Builder(object):
    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError


class BuilderHouse(Builder):
    def build_floor(self):
        self.building.floor = 'One'

    def build_size(self):
        self.building.size = 'Big'


class BuilderFlat(Builder):

    def build_floor(self):
        self.building.floor = 'More than One'

    def build_size(self):
        self.building.size = 'Small'


if __name__ == '__main__':
    building = construct_building(BuilderHouse())
    print(building)
    building = construct_building(BuilderFlat())
    print(building)