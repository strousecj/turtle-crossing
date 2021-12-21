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

car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if car_manager.num_cars < 25:
        car_manager.generate_car()

    car_manager.move_cars()

    for i in range(0, len(car_manager.car_list-1)):
        # TODO: improve car hit detection
        if player.distance(car_manager.car_list[i]) <= 25:
            game_is_on = False

        if car_manager.car_list[i-1].xcor() < -320:
            car_manager.remove_car(i)

    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.reset_to_start()

scoreboard.game_over()
screen.exitonclick()
