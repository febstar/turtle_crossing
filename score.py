from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-275, 275)
        self.scores = 0
        self.write(f"Score: {self.scores}", move=False, align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=('Spooky', 20, 'normal'))

    def update(self):
        self.clear()
        self.scores += 1
        self.write(f"Score: {self.scores}", move=False, align='center', font=('Arial', 20, 'normal'))
