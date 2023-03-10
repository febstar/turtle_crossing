from turtle import Turtle
import turtle
import random
turtle.colormode(255)
STARTING_SPPED = 5
MOVE_INCRE = 10


class Cars:

    def __init__(self):
        self.list = []
        self.create_car()
        self.speed = STARTING_SPPED

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            n = Turtle()
            n.penup()
            n.shape("square")
            n.shapesize(stretch_wid=1, stretch_len=2)
            n.setheading(180)
            n.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.list.append(n)
            self.gotorand(n)



    def move(self):
        for car in range(len(self.list)):
            self.list[car].forward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCRE

    def gotorand(self, n):
        n.goto(random.randint(350, 400), random.randint(-200, 240))