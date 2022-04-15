from tkinter import *
import random
import time


class Boss:
    board = None
    image = None

    last_move = time.time()

    d6 = 1
    Level = 1

    HP = 2 * Level * d6 + d6
    DP = Level / 2 * d6 + d6 / 2
    SP = Level * d6 + Level

    x = 0
    y = 0

    def __init__(self, board):
        self.board = board
        self.image = PhotoImage(file="images/boss.png")
        self.image = self.image.subsample(2)

        self.init_random()

    def init_random(self):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.board.map[y][x] != "w":
                if x or y:
                    self.x = x
                    self.y = y
                    break

    def move(self):
        direction = random.randint(0, 4)
        if direction == 0 and self.x < 9 and self.board.map[self.y][self.x+1] == "f":
            self.x += 1
        elif direction == 1 and self.x > 0 and self.board.map[self.y][self.x-1] == "f":
            self.x -= 1
        elif direction == 2 and self.y < 9 and self.board.map[self.y+1][self.x] == "f":
            self.y += 1
        elif direction == 3 and self.y > 0 and self.board.map[self.y-1][self.x] == "f":
            self.y -= 1

    def refresh(self):
        if time.time() - self.last_move > 1:
            self.last_move = time.time()
            self.move()
        x = self.x * self.board.image_size
        y = self.y * self.board.image_size
        self.board.canvas.create_image(x, y, image=self.image, anchor=NW)
