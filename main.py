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

gamespped = [0.1, 0.09, 0.08, 0.07]
game_is_on = True


while game_is_on:

    car.create_car()
    screen.update()
    time.sleep(0.08)
    car.move()

    if play.ycor() > 290:
        play.reset_self()
        scorer.update()

    for cars in car.list:
        if play.distance(cars) < 15:
            scorer.game_over()
            game_is_on = False

    if scorer.scores >= 5:
        time.sleep(random.choice(gamespped))



screen.exitonclick()