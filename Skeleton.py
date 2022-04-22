from tkinter import *
import random
import time
from Sprite import *


class Skeleton(Sprite):
    game = None
    image = None
    image_key = None

    last_move = time.time()
    previous_move = [0, 0]

    d6 = 1
    Level = 1

    key = False

    last_move = 0

    _HP = 2 * Level * d6
    DP = Level / 2 * d6
    SP = Level * d6

    def __init__(self, game):
        super().__init__(game)
        game.sprite(skeleton=self)

        self.image = PhotoImage(file="images/skeleton.png")
        self.image = self.image.subsample(2)

        self.image_key = PhotoImage(file="images/key.png")
        self.image_key = self.image_key.subsample(2)

        self.random_location()

    @property
    def HP(self):
        return self._HP

    @HP.setter
    def HP(self, a):
        if self._HP > 0 and a <= 0:
            self.death()

        if a <= 0:
            self._HP = 0
        else:
            self._HP = a

    def death(self):
        print("The skeleton is dead.")

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

        if self.key:
            self.game.canvas.create_image(
                x, y, image=self.image_key, anchor=NW)
