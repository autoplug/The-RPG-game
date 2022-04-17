from Hero import *
from Boss import *
from Skeleton import *
from Game import *

game = Game()
hero = Hero(game)
boss = Boss(game)
skeleton = Skeleton(game)

game.sprite(hero=hero, boss=boss, skeleton=skeleton)

while True:
    game.update()

    if game.quit:
        break
