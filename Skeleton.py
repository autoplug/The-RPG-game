from Character import *


class Skeleton(Character):
    game = None
    image = None
    image_key = None

    def __init__(self, game, key=False):
        super().__init__(game)
        game.get_character(skeleton=self)
        self.key = key
        self.image = self.game.load_image("images/skeleton.png")
        self.image_key = self.game.load_image("images/key.png")

        self.level_stats()

    def level_stats(self):
        self.random_location()

        self.d6 = random.randint(1, 6)
        self.HP = 2 * self.game.Level * self.d6
        self.MaxHP = self.HP
        self.DP = (self.game.Level / 2) * self.d6
        self.SP = self.game.Level * self.d6

    def update(self):
        if self.HP <= 0:
            return
        self.random_move()

        self.game.draw_image(self)
