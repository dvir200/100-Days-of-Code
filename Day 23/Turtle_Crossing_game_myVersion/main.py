from car import Car
from turtle import Screen
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("grey")
screen.tracer(0)


car1 = Car()
car2 = Car()
while True:

    car1.move()
    car2.move()
    screen.update()
    time.sleep(1)

screen.exitonclick()