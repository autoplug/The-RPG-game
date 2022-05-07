from tkinter import *
from Character import *
import random


class Boss(Character):
    game = None
    image = None

    def __init__(self, game):
        super().__init__(game)
        game.get_character(boss=self)
        self.image = PhotoImage(file="images/boss.png").subsample(2)

        self.level_stats()

    def level_stats(self):
        self.random_location()
        self.d6 = random.randint(1, 6)
        self.HP = 2 * self.game.Level * self.d6 + self.d6
        self.MaxHP = self.HP
        self.DP = self.game.Level / 2 * self.d6 + self.d6 / 2
        self.SP = self.game.Level * self.d6 + self.game.Level

    def update(self):
        if self.HP <= 0:
            return
        self.random_move()
        self.game.draw_image(self)
