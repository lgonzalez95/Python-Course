import random


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        return random.randint(1, self.sides)


d = Dice(6)
print(d.roll_dice())
