# -*- coding: utf-8 -*-
# Author: kai.zhang01
# Date: 2018/8/23 
# Desc:

import random

class PetShop(object):
    def __init__(self, animal_factory=None):
        self.pet_factory = animal_factory

    def show_pet(self):
        pet = self.pet_factory()
        print('We have a lovely {}'.format(pet))
        print('It says {}'.format(pet.speak()))

class Dog(object):
    def speak(self):
        return 'woof'

    def __str__(self):
        return 'Dog'

class Cat(object):
    def speak(self):
        return 'meow'

    def __str__(self):
        return 'Cat'

def random_animal():
    return random.choice([Dog, Cat])()

class Trade(object):
    def __init__(self, exchange_hander = None):
        self.exchnage_factory = exchange_hander
        self.client = self.exchnage_factory()


    def trade(self, ):
        self.client.trade()


class Binance(object):
    def __init__(self):
        pass
    def trade(self):
        print('binance trade..')

class Okex(object):
    def __init__(self):
        pass
    def trade(self):
        print('Okex trade..')



if __name__ == '__main__':
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()

    print('-------------------')
    shop = PetShop(random_animal)
    for i in range(3):
        shop.show_pet()
        print('=' * 20)

    tr = Trade(Okex)
    tr.trade()






