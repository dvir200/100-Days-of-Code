from car import Cars
from player import PlayerChar
from turtle import Screen
from scoreboard import Scoreboard
import time

UP_KEY = "Up"

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("grey")
screen.tracer(0)

scoreboard = Scoreboard()
car_array = Cars()
car_array.add_car()
Player_char = PlayerChar()

screen.listen()
screen.onkey(fun=Player_char.move_forward, key=UP_KEY)

is_player_alive = True

while is_player_alive:
    time.sleep(0.1)
    car_array.move_cars()
    screen.update()
    car_array.add_car()

    if Player_char.ycor() > 280:
        scoreboard.update()
        car_array.increase_speed()
        Player_char.reset_pos()

    else:
        for item in car_array.cars_list:
            if item.distance(Player_char) < 25:
                car_array.stop_cars()
                scoreboard.end_game()
                is_player_alive = False

screen.exitonclick()