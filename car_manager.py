from turtle import Turtle
import random

COLORS = ["red", "orange", "gold", "green", "blue", "purple"]
MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.car_list = []
        self.move_distance = MOVE_DISTANCE

    def generate_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.goto(300, random.randint(-250, 250))
        car.setheading(180)
        self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.move_distance)

    def remove_car(self, car_num):
        self.car_list.pop(car_num)

    def increase_car_speed(self):
        self.move_distance += MOVE_INCREMENT
