from turtle import Turtle
import turtle
import random
turtle.colormode(255)


class Cars():

    def __init__(self):
        self.list = []
        self.create_car()


    def create_car(self):
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
            self.list[car].forward(15)

    def gotorand(self, n):
        n.goto(random.randint(350, 400), random.randint(-200, 240))