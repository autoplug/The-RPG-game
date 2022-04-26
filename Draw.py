from tkinter import *


class Draw:

    root = None

    def init(self):
        root = Tk()
        root.title('Wanderer Game')
        return root

    def load_image(self, path):
        image = PhotoImage(file=path)
        image = image.subsample(2)
        return image
