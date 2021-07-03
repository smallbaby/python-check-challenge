# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Desc:
sla_job = ['A', 'B',  'D', ]  # SLA 下的任务列表
root_job = ['A']  # root节点
dependents = [['A', 'B'], ['B', 'D'], ['C', 'E'], ['A', 'C'], ['B', 'D'], ['B', 'F']]  # 依赖关系 => 父   子
map = {}  # 临时map
chains = []  # 链路集合


def getChildren(node):  # 获取节点的子节点列表
    return [x[1] for x in dependents if x[0] == node]

def loopRelationship(node):
    temp = []
    if node in map:
        temp = map[node]  # 上一个节点的上游链
    childs = getChildren(node)
    if not childs:
        chains.append(temp)
        return
    for x in childs:
        if x not in sla_job:
            if node not in root_job:  # 去掉root节点的链路
                chains.append(temp)
            continue
        else:
            map[x] = temp + [x]
            loopRelationship(x)


def main():
    for root in root_job:
        map[root] = [root]
        res = []
        loopRelationship(root)
    for chain in chains:
        print(chain)


if __name__ == '__main__':
    main()