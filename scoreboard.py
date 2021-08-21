from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(). __init__()
        self.penup()
        self.hideturtle()
        self.goto(-300, 260)
        # self.write("Level: ", align="left", font=FONT)

    def score(self, x):
        self.clear()
        self.write(f"Level: {x}", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)

