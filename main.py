import random
from turtle import Screen
from cars import Cars
from score import Score
from player import Player
import time

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.listen()
screen.tracer(0)

car = Cars()
play = Player()
scorer = Score()
screen.onkey(fun=play.move, key="Up")

game_is_on = True


while game_is_on:

    car.create_car()
    screen.update()
    car.move()
    screen.update()
    time.sleep(0.1)

    if play.ycor() > 290:
        play.reset_self()
        scorer.update()
        car.level_up()

    for cars in car.list:
        if play.distance(cars) < 15:
            scorer.game_over()
            game_is_on = False





screen.exitonclick()