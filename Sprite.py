from tkinter import *
import random
import time


class Sprite:
    image = None
    image_size = 32

    delay = 1
    last_move = time.time()

    x = 0
    y = 0

    game = None

    def __init__(self, game):
        self.game = game

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
