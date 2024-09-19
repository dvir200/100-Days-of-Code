from turtle import Screen, Turtle
from pong_ball import Ball
import time


screen = Screen()
screen.setup(width= 900, height=500)
screen.title("Pong Game")
screen.bgcolor("black")
""" screen.tracer(0) """

is_game_on = True

ball = Ball()
""" screen.update() """
while is_game_on:
  ball.movement()
  if (ball.head.ycor() == 200.0) or (ball.head.ycor() == -200.0):
    ball.head.change_direction()



""" while is_game_on:
  screen.update()
  time.sleep(0.1)
  ball.movement() """


screen.exitonclick()