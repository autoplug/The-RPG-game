from tkinter import *
from Character import *
import random


class Hero(Character):
    game = None

    def __init__(self, game):
        super().__init__(game)
        game.get_character(hero=self)

        self.image_down = PhotoImage(file="images/hero-down.png").subsample(2)
        self.image_up = PhotoImage(file="images/hero-up.png").subsample(2)
        self.image_left = PhotoImage(file="images/hero-left.png").subsample(2)
        self.image_right = PhotoImage(
            file="images/hero-right.png").subsample(2)

        self.delay = 0.5

        self.level_stats()

    def level_stats(self):
        self.image = self.image_down
        self.x = 0
        self.y = 0
        self.d6 = random.randint(1, 6)
        self.HP = 20 + 3 * self.d6
        self.MaxHP = self.HP
        self.DP = 2 * self.d6
        self.SP = 5 + self.d6

    def move(self, event):
        self.game.hero_movement += 1
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
