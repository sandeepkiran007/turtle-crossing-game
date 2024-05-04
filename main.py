from turtle import Screen
import time
from player import Player
from cars_manager import Cars
from scoreboard import ScoreBoard
scr = Screen()
scr.screensize(600, 600)
scr.bgpic('background.png')
scr.tracer(0)
scr.listen()


is_game_over = False
player = Player()
cars = Cars()
scoreboard = ScoreBoard()

scr.onkey(player.move, 'Up')
while not is_game_over:
    scr.update()
    time.sleep(0.1)
    cars.generate_random_car()
    cars.move()

    # detect collision with car
    for car in cars.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            is_game_over = True
    # detect level up
    if player.ycor() > 230:
        player.reset()
        scoreboard.level_up()
        cars.speed_up()
scr.exitonclick()