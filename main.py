import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()

player = Player()
screen.onkeypress(player.move_forward, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.reset_to_start()


scoreboard.game_over()

screen.exitonclick()
