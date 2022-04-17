from tkinter import *
import random
import time
from Sprite import *


class Skeleton(Sprite):
    game = None
    image = None
    image_key = None

    d6 = 1
    Level = 1

    key = False

    last_move = 0

    _HP = 2 * Level * d6
    DP = Level / 2 * d6
    SP = Level * d6

    def __init__(self, game):
        self.game = game
        game.sprite(skeleton=self)

        self.image = PhotoImage(file="images/skeleton.png")
        self.image = self.image.subsample(2)

        self.image_key = PhotoImage(file="images/key.png")
        self.image_key = self.image_key.subsample(2)

        self.init_random()

    def init_random(self):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.game.map[y][x] != "w":
                if x or y:
                    self.x = x
                    self.y = y
                    break

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

    def move(self):
        while True:
            direction = random.randint(0, 4)
            if direction == 0 and self.x < 9 and self.game.map[self.y][self.x+1] == "f":
                self.x += 1
                break
            elif direction == 1 and self.x > 0 and self.game.map[self.y][self.x-1] == "f":
                self.x -= 1
                break
            elif direction == 2 and self.y < 9 and self.game.map[self.y+1][self.x] == "f":
                self.y += 1
                break
            elif direction == 3 and self.y > 0 and self.game.map[self.y-1][self.x] == "f":
                self.y -= 1
                break

    def strike(self, sprite=None):
        if not sprite:
            return
        if self.SP >= sprite.DP:
            sprite.HP -= 1

    def update(self):
        if self.HP <= 0:
            return
        if time.time() - self.last_move > 1:
            self.last_move = time.time()
            self.move()

        x = self.x * self.game.image_size
        y = self.y * self.game.image_size
        self.game.canvas.create_image(x, y, image=self.image, anchor=NW)

        if self.key:
            self.game.canvas.create_image(
                x, y, image=self.image_key, anchor=NW)
