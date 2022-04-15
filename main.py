from tkinter import *
from Board import *
from Hero import *
from Boss import *
from Skeleton import *


root = Tk()
root.title('Wanderer Game')

board = Board(root)
hero = Hero(board)
boss = Boss(board)
skeleton = Skeleton(board)

root.bind("<Key>", hero.move)

while True:
    board.refresh()
    hero.refresh()
    boss.refresh()
    skeleton.refresh()

    root.update_idletasks()
    root.update()
