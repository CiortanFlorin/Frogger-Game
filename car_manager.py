import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super(). __init__()
        self.shape("square")
        self.penup()
        self.shapesize(1, 2, 1)
        self.color(random.choice(COLORS))
        self.seth(180)
        self.goto(300, random.randint(-250, 250))

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def speed_increase(self):
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT