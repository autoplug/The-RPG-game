from tkinter import *
from PIL import Image, ImageTk


class Draw:
    labels = []
    floor = None
    wall = None
    image_width = 72
    hero = [0, 0]

    def __init__(self, matrix, window):
        self.window = window
        load = Image.open("images/floor.png")
        self.floor = ImageTk.PhotoImage(load)

        load = Image.open("images/wall.png")
        self.wall = ImageTk.PhotoImage(load)

        for x in range(10):
            for y in range(10):
                if (x+y) % 2:
                    self.block(self.wall, x, y)
                else:
                    self.block(self.floor, x, y)

        self.move(0, 0)

    def block(self, render, x, y):
        # load = Image.open("images/floor.png")
        # render = ImageTk.PhotoImage(load)
        img = Label(self.window, image=render)
        img.image = render
        img.place(x=x*72, y=y*72)
        return img

    def move(self, x, y):
        load = Image.open("images/hero-down.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self.window, image=render)
        img.image = render
        img.place(x=x*72, y=y*72)
        pass
