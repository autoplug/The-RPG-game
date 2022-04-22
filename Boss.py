from tkinter import *
import random
import time
from Sprite import *


class Boss(Sprite):
    game = None
    image = None

    last_move = time.time()
    previous_move = [0, 0]

    d6 = 1
    Level = 1

    _HP = 2 * Level * d6 + d6
    DP = Level / 2 * d6 + d6 / 2
    SP = Level * d6 + Level

    x = 0
    y = 0

    def __init__(self, game):
        super().__init__(game)
        game.sprite(boss=self)

        self.image = PhotoImage(file="images/boss.png")
        self.image = self.image.subsample(2)

        self.random_location()

    @property
    def HP(self):
        return self._HP

    @HP.setter
    def HP(self, value):
        if self._HP > 0 and value <= 0:
            print("The boss Died.")

        if value <= 0:
            self._HP = 0
        else:
            self._HP = value

    def strike(self, sprite=None):
        if not sprite:
            return
        if self.SP >= sprite.DP:
            sprite.HP -= 1

    def update(self):
        if self.HP <= 0:
            return
        self.random_move()
        x = self.x * self.game.image_size
        y = self.y * self.game.image_size
        self.game.canvas.create_image(x, y, image=self.image, anchor=NW)