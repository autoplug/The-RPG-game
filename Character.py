from tkinter import *
import random
import time


class Character:
    image = None
    image_size = 32

    movement = 0

    key = False

    delay = 1
    last_move = time.time()
    last_location = [0, 0]

    x = 0
    y = 0

    game = None

    __HP = 0
    DP = 0
    SP = 0

    def __init__(self, game):
        self.game = game

    @property
    def HP(self):
        return self.__HP

    @HP.setter
    def HP(self, hp):
        if self.__HP > 0 and hp <= 0:
            print("The character is dead.")

        if hp <= 0:
            self.__HP = 0
        else:
            self.__HP = hp

    def strike(self, character):
        d6 = random.randint(1, 6)
        # The strike is successful if 2 * d6 + SP is higher than the other character's DP.
        if (2 * d6 + self.SP) >= character.DP:
            character.HP -= self.SP
            # After a hero character performed a strike the defender should strike back the same way
            if (2 * d6 + character.SP) >= self.DP:
                self.HP -= character.SP

    def random_location(self):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.game.map[y][x] != "w":
                if x or y:
                    self.x = x
                    self.y = y
                    break
        return [x, y]

    def random_move(self):
        # After every two move, the monsters move one tile as well.
        if self.game.hero_movement-self.movement < 2:
            return
        self.movement = self.game.hero_movement

        while True:
            direction = ["Right", "Left", "Up", "Down"]
            direction = direction[random.randint(0, 3)]
            move_location = self.game.move_permit(
                direction=direction, x=self.x, y=self.y)

            # for fluent movement
            if self.last_location == move_location and random.randint(0, 15):
                move_location = False

            if move_location:
                self.last_location = [self.x, self.y]
                [self.x, self.y] = move_location
                break
