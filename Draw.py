from tkinter import *


class Draw:

    root = None

    def init(self):
        root = Tk()
        root.title('Wanderer Game')
        return root

    @staticmethod
    def load_image(path):
        image = PhotoImage(file=path)
        image = image.subsample(2)
        return image
