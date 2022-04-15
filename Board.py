from tkinter import *


class Board:
    map = []
    image_size = 36

    def __init__(self, window):
        self.window = window
        width = self.image_size * 10
        height = self.image_size * 10 + 50
        self.canvas = Canvas(window, bg="black", width=width, height=height)
        self.canvas.pack()
        self.load_map()

        self.floor = PhotoImage(file="images/floor.png")
        self.floor = self.floor.subsample(2)

        self.wall = PhotoImage(file="images/wall.png")
        self.wall = self.wall.subsample(2)

    def load_map(self):
        file_map = open("map.txt", "r")
        file_map = file_map.read()
        file_map = file_map.split("\n")
        for line in range(len(file_map)):
            self.map.append([])
            for char in file_map[line]:
                self.map[line].append(char)

    def refresh(self):
        self.canvas.delete("all")
        for x in range(10):
            for y in range(10):
                x1 = x * self.image_size
                y1 = y * self.image_size
                if self.map[y][x] == "w":
                    self.canvas.create_image(
                        x1, y1, image=self.wall, anchor=NW)
                else:
                    self.canvas.create_image(
                        x1, y1, image=self.floor, anchor=NW)
