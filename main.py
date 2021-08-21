import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard1 = Scoreboard()
scoreboard2 = Scoreboard()
screen.listen()
screen.onkey(player.move, "w")

cars = []
i=0
game_is_on = True
while game_is_on:
    i += 1
    time.sleep(0.1)
    screen.update()
    if i%7 == 0:
        car = CarManager()
        cars.append(car)
    for car in cars:
        car.move()
        if player.distance(car) < 20:
            scoreboard2.game_over()
            game_is_on=False
    player.reset()
    scoreboard1.score(player.score)
screen.exitonclick()