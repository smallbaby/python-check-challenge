# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Desc:

# 生成器也是迭代器的一种,但是你只能迭代它们一次.原因很简单,
# 因为它们不是全部存在内存里,它们只在要调用的时候在内存里生成
# 生成器和迭代器的区别就是用()代替[]
mygenerator = (x * x for x in range(3))
for i in mygenerator:
    print(i)


def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i * i


mygenerator = createGenerator()  # 创建生成器
for i in mygenerator:
    print(i)


#######


def shout(word="yes"):
    return word.capitalize() + "!"


# print(shout())

# talk()


def dosomething(func):
    print('before')
    func()
    print('after')


@dosomething
def talk():
    # 你可以在"talk"里定义另一个函数 ...
    def whisper(word="YES"):
        return word.lower() + "..."

    # 让我们用用它!

    print(whisper())


talk()
