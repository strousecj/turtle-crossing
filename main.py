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
cars_to_delete = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if len(car_manager.car_list) < 20:
        car_manager.generate_car()

    car_manager.move_cars()

    for i in range(0, len(car_manager.car_list) - 1):
        # TODO: improve car hit detection
        if player.distance(car_manager.car_list[i]) <= 25:
            game_is_on = False

        if car_manager.car_list[i].xcor() < -320:
            cars_to_delete.append(i)

    cars_to_delete.sort(reverse=True)
    for car_index in cars_to_delete:
        car_manager.remove_car(car_index)

    cars_to_delete.clear()

    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.reset_to_start()

scoreboard.game_over()
screen.exitonclick()
