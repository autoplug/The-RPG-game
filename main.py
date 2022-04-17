from Hero import *
from Boss import *
from Skeleton import *
from Game import *

game = Game()
hero = Hero(game)
boss = Boss(game)
skeleton1 = Skeleton(game)
skeleton1.key = True
skeleton2 = Skeleton(game)
skeleton3 = Skeleton(game)


while True:
    game.update()

    if game.quit:
        break
