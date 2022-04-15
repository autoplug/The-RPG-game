from Board import Draw
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Game")

draw = Draw(root)

root.bind("<Key>", lambda x: draw.move(x.keycode))

root.mainloop()
