from turtle import Turtle
import car_manager
STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 260


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.seth(90)
        self.score = 0
    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.score += 1
            car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT