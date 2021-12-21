from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []

    def generate_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.goto(random.randint(300, 600), random.randint(-270, 270))
        car.setheading(180)
        self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(MOVE_DISTANCE)

    def remove_car(self, car_num):
        self.car_list.pop(car_num)
