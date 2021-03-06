from tkinter import *


class Game:
    map = []
    image_size = 36

    window = None

    quit = False

    Level = 1

    hero = None
    boss = None
    skeletons = []

    hero_movement = 0

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

        self.label = Label(self.window, text="")
        self.label.pack()

        self.floor = PhotoImage(file="images/floor.png").subsample(2)
        self.wall = PhotoImage(file="images/wall.png").subsample(2)

    def load_map(self):
        file_map = open(f"maps/{self.Level}.txt", "r")
        self.map = file_map.readlines()
        file_map.close()

    def draw_image(self, character):
        x = character.x * self.image_size
        y = character.y * self.image_size
        self.canvas.create_image(x, y, image=character.image, anchor=NW)

        # this is skeleton with key
        if character.key:
            self.canvas.create_image(
                x, y, image=character.image_key, anchor=NW)

    def get_character(self, hero=None, boss=None, skeleton=None):
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
            character = self.collide()
            if character:
                self.hero.strike(character)
                character.strike(self.hero)
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
        self.label["text"] += f"Level    : {self.Level}\n"
        self.label["text"] += f"Hero HP: {self.hero.HP}/{self.hero.MaxHP} | DP: {self.hero.DP} | SP: {self.hero.SP}\n"
        self.label['text'] += f"Boss HP: {self.boss.HP}/{self.boss.MaxHP} | DP: {self.boss.DP} | SP: {self.boss.SP}\n"
        for skeleton in self.skeletons:
            self.label['text'] += f"Skeleton HP: {skeleton.HP}/{skeleton.MaxHP} | DP: {skeleton.DP} | SP: {skeleton.SP}\n"

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
        # When the enemy with the key is killed, the hero should enter the new level automatically
        if self.boss.HP == 0:
            for skeleton in self.skeletons:
                if skeleton.key and skeleton.HP == 0:
                    self.Level += 1
                    self.hero.x = 0
                    self.hero.y = 0
                    self.hero.level_stats()
                    for character in [*self.skeletons, self.boss]:
                        character.level_stats()
                        character.random_location()
                    self.load_map()

    def update(self):
        self.collide()
        self.draw_menu()
        self.next_level()

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

        for character in [*self.skeletons, self.boss, self.hero]:
            character.update()

        self.window.update_idletasks()
        self.window.update()
