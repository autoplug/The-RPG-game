from tkinter import *
from Character import *
import random


class Hero(Character):
    game = None
    image = None
    image_down = None
    image_up = None
    image_left = None
    image_right = None

    def __init__(self, game):
        super().__init__(game)
        game.get_character(hero=self)

        self.image_down = self.game.load_image("images/hero-down.png")
        self.image_up = self.game.load_image("images/hero-up.png")
        self.image_left = self.game.load_image("images/hero-left.png")
        self.image_right = self.game.load_image("images/hero-right.png")

        self.image = self.image_down
        self.delay = 0.5

        self.d6 = random.randint(1, 6)
        self.HP = 20 + 3 * self.d6
        self.DP = 2 * self.d6
        self.SP = 5 + self.d6

    def move(self, event):
        if self.game.move_permit(direction=event.keysym, x=self.x, y=self.y):
            [self.x, self.y] = self.game.move_permit(
                direction=event.keysym, x=self.x, y=self.y)
            if event.keysym == "Right":
                self.image = self.image_right
            elif event.keysym == "Left":
                self.image = self.image_left
            elif event.keysym == "Down":
                self.image = self.image_down
            elif event.keysym == "Up":
                self.image = self.image_up

    def update(self):
        self.game.draw_image(self)
