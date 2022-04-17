from tkinter import *
from Sprite import *
import random


class Hero(Sprite):
    game = None
    image = None
    image_down = None
    image_up = None
    image_left = None
    image_right = None

    move_count = 0

    d6 = 2
    __HP = 20 + 3 * d6
    __DP = 2 * d6
    __SP = 5 + d6

    x = 0
    y = 0

    def __init__(self, game):
        self.game = game
        game.sprite(hero=self)

        self.HP = 20 + 3 * random.randint(1, 6)

        self.image_down = PhotoImage(file="images/hero-down.png")
        self.image_down = self.image_down.subsample(2)

        self.image_up = PhotoImage(file="images/hero-up.png")
        self.image_up = self.image_up.subsample(2)

        self.image_left = PhotoImage(file="images/hero-left.png")
        self.image_left = self.image_left.subsample(2)

        self.image_right = PhotoImage(file="images/hero-right.png")
        self.image_right = self.image_right.subsample(2)

        self.image = self.image_down

    def move(self, event):
        self.move_count += 1
        if event.keysym == "Right":
            self.image = self.image_right
            if self.x < 9 and self.game.map[self.y][self.x+1] != "w":
                self.x += 1
        elif event.keysym == "Left":
            self.image = self.image_left
            if self.x > 0 and self.game.map[self.y][self.x-1] != "w":
                self.x -= 1
        elif event.keysym == "Down":
            self.image = self.image_down
            if self.y < 9 and self.game.map[self.y+1][self.x] != "w":
                self.y += 1
        elif event.keysym == "Up":
            self.image = self.image_up
            if self.y > 0 and self.game.map[self.y-1][self.x] != "w":
                self.y -= 1

    # HP prperty
    @property
    def HP(self):
        return self.__HP

    @HP.setter
    def HP(self, value):
        if self.__HP > 0 and value <= 0:
            print("hero is died.")
            value = 0
        self.__HP = value

    # DP prperty
    @property
    def DP(self):
        return 2 * random.randint(1, 6)

    # SP prperty  5 + d6
    @property
    def SP(self):
        return 5 + random.randint(1, 6)

    def strike(self, sprite=None):
        if not sprite:
            return
        if self.SP >= sprite.DP:
            sprite.HP -= self.SP

    def update(self):
        x = self.x * self.game.image_size
        y = self.y * self.game.image_size
        self.game.canvas.create_image(x, y, image=self.image, anchor=NW)
