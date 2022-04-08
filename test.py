from tkinter import *

# pip install pillow
from PIL import Image, ImageTk


root = Tk()
load = Image.open("images/floor.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.image = render
img.place(x=0, y=0)

root.title("Tkinter window")
root.geometry("200x120")
root.mainloop()
