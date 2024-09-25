from turtle import Turtle
import random

COLORS = ["blue", "black","white", "red", "yellow", "green", "purple", "pink"]
STEPS = 10
STEP_INCREASE = 5

class Cars:
    def __init__(self):
        self.cars_list = []

    def add_car(self):
        rand_value = random.randint(0,4)
        if rand_value == 1:
            vehicle = Turtle()
            vehicle.shape("square")
            vehicle.shapesize(stretch_wid=1, stretch_len=2)
            vehicle.penup()
            vehicle.setheading(180)
            vehicle.goto(x=420, y=random.randint(-250, 280))
            vehicle.color(random.choice(COLORS))
            if len(self.cars_list) == 0:
                self.cars_list.append(vehicle)
            else:
                for item in self.cars_list:
                    if item.xcor() < -420:
                        item = vehicle
                        pass
                self.cars_list.append(vehicle)

    def move_cars(self):
        for item in self.cars_list:
            item.forward(STEPS)

    def increase_speed(self):
        global STEPS
        STEPS = STEPS + STEP_INCREASE

    def stop_cars(self):
        for item in self.cars_list:
            item.forward(0)
