from tkinter import *


class Hero:
    board = None
    image = None
    image_down = None
    image_up = None
    image_left = None
    image_right = None

    move_count = 0

    d6 = 2
    HP = 20 + 3 * d6
    DP = 2 * d6
    SP = 5 + d6

    x = 0
    y = 0

    def __init__(self, board):
        self.board = board
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
        if event.keycode == 2080438019:
            self.image = self.image_right
            if self.x < 9 and self.board.map[self.y][self.x+1] != "w":
                self.x += 1
        elif event.keycode == 2063660802:
            self.image = self.image_left
            if self.x > 0 and self.board.map[self.y][self.x-1] != "w":
                self.x -= 1
        elif event.keycode == 2097215233:
            self.image = self.image_down
            if self.y < 9 and self.board.map[self.y+1][self.x] != "w":
                self.y += 1
        elif event.keycode == 2113992448:
            self.image = self.image_up
            if self.y > 0 and self.board.map[self.y-1][self.x] != "w":
                self.y -= 1

    def refresh(self):
        x = self.x * self.board.image_size
        y = self.y * self.board.image_size
        self.board.canvas.create_image(x, y, image=self.image, anchor=NW)
