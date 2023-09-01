from abc import ABC


class Robot(ABC):
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hi ', self.name)


class PoliceRobot(Robot):
    def say_hi(self):
        print('Hi, I\'m a police robot, my name is', self.name)


pl = PoliceRobot('Pochita')
pl.say_hi()
