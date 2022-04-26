from tkinter import *


class Draw:

    @staticmethod
    def init():
        root = "plpl"
        # root = Tk()
        # root.title('Wanderer Game')
        return root

    root = init()

    @staticmethod
    def load_image(path):
        image = PhotoImage(file=path)
        image = image.subsample(2)
        return image
