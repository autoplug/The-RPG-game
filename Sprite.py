from tkinter import *
import random
import time


class Sprite:
    image = None
    image_size = 32

    __x = 0
    __y = 0
    game = None

    delay = 1

    def __init__(self, game):
        self.game = game

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def strike(self, sprite=None):
        if not sprite:
            return
        if self.SP >= sprite.DP:
            sprite.HP -= 1

    def random_location(self):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.game.map[y][x] != "w":
                if x or y:
                    self.x = x
                    self.y = y
                    break

    def random_move(self):
        if time.time() - self.last_move < self.delay:
            return

        self.last_move = time.time() + random.randint(0, 20)/20
        while True:
            direction = ["Right", "Left", "Up", "Down"]
            direction = direction[random.randint(0, 3)]
            if self.game.move_permit(direction=direction, x=self.x, y=self.y):
                [self.x, self.y] = self.game.move_permit(
                    direction=direction, x=self.x, y=self.y)
                break
