from Game import *
from Hero import *
from Boss import *
from Skeleton import *


game = Game()
hero = Hero(game)
boss = Boss(game)

# skeleton with the key
skeleton1 = Skeleton(game, True)

skeleton2 = Skeleton(game)
skeleton3 = Skeleton(game)


while True:
    game.update()

    if game.quit:
        break
