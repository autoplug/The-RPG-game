from draw import *
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Hello")

canvas = Canvas(root, width=500, height=500)
canvas.pack()

n = 10
matrix = [[0 for i in range(n)] for j in range(n)]
draw = Draw(matrix, root)

root.bind("<Key>", lambda x: print(x.keycode))

root.mainloop()
