from tkinter import *


class Sprite:
    image = None
    image_size = 32

    __x = 0
    __y = 0

    def __init__(self):
        pass

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
