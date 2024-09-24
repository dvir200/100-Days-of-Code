from car import Cars
from player import PlayerChar
from turtle import Screen
import time

UP_KEY = "Up"

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("grey")
screen.tracer(0)

car_array = Cars()
car_array.add_car()

Player_char = PlayerChar()

screen.listen()
screen.onkey(fun=Player_char.move_forward, key=UP_KEY)

while True:
    time.sleep(0.1)
    car_array.move_cars()
    screen.update()
    car_array.add_car()

    if Player_char.ycor() > 300:
        car_array.increase_speed()
        Player_char.reset_pos()

screen.exitonclick()