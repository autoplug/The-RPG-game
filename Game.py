from tkinter import *


class Game:
    map = []
    image_size = 36

    window = None

    level = 1

    quit = False

    hero = None
    boss = None
    skeletons = []

    def __init__(self):
        self.window = Tk()
        self.window.title('Wanderer Game')
        self.window.bind("<Key>", self.keypress)

        width = self.image_size * 10
        height = self.image_size * 10
        self.canvas = Canvas(self.window, bg="black",
                             width=width, height=height)
        self.canvas.pack()
        self.load_map()

        self.label = Label(self.window, text="Health : 0")
        self.label.pack()

        self.floor = PhotoImage(file="images/floor.png")
        self.floor = self.floor.subsample(2)

        self.wall = PhotoImage(file="images/wall.png")
        self.wall = self.wall.subsample(2)

    def load_map(self):
        file_map = open("maps/1.txt", "r")
        file_map = file_map.read()
        file_map = file_map.split("\n")
        for line in range(len(file_map)):
            self.map.append([])
            for char in file_map[line]:
                self.map[line].append(char)

    def sprite(self, hero=None, boss=None, skeleton=None):
        if hero:
            self.hero = hero
        if boss:
            self.boss = boss
        if skeleton:
            self.skeletons.append(skeleton)

    def keypress(self, event):
        if event.keysym == "Escape":
            self.quit = True
        if event.keysym == "space":
            sprite = self.collide()
            if sprite:
                self.hero.strike(sprite)
                sprite.strike(self.hero)
        else:
            self.hero.move(event)

    def collide(self):
        if self.boss.HP > 0 and self.hero.x == self.boss.x and self.hero.y == self.boss.y:
            return self.boss
        for skeleton in self.skeletons:
            if skeleton.HP > 0 and self.hero.x == skeleton.x and self.hero.y == skeleton.y:
                return skeleton
        return None

    def draw_menu(self):
        self.label["text"] = ""
        self.label["text"] += "Level    : " + str(self.hero.Level) + '\n'
        self.label["text"] += "Hero     : " + str(self.hero.HP) + '\n'
        self.label['text'] += "Boss     : " + str(self.boss.HP) + '\n'
        for skeleton in self.skeletons:
            self.label['text'] += "Skeleton : " + str(skeleton.HP) + '\n'

    def move_permit(self, direction="Right", x=0, y=0):
        if direction == "Right" and x < 9 and self.map[y][x+1] != "w":
            return [x+1, y]
        if direction == "Left" and x > 0 and self.map[y][x-1] != "w":
            return [x-1, y]
        if direction == "Down" and y < 9 and self.map[y+1][x] != "w":
            return [x, y+1]
        if direction == "Up" and y > 0 and self.map[y-1][x] != "w":
            return [x, y-1]
        return False

    def next_level(self):
        print("You success to go to the next level.")

    def update(self):
        self.collide()
        self.draw_menu()

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

        self.hero.update()
        self.boss.update()
        for skeleton in self.skeletons:
            skeleton.update()

        self.window.update_idletasks()
        self.window.update()
