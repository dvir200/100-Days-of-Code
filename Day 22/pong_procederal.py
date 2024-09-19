from turtle import Turtle, Screen
import time
import random

def up_player1():
  player1.setheading(90)
  player1.forward(30)

def down_player1():
  player1.setheading(270)
  player1.forward(30)

def up_player2():
  player2.setheading(90)
  player2.forward(30)

def down_player2():
  player2.setheading(270)
  player2.forward(30)


screen = Screen()
screen.setup(width=1000, height=480)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

is_game_on = True
initial_heading = random.randrange(0, 360)
screen.update()

ball = Turtle()
ball.penup()
ball.shape("circle")
ball.color("white")
ball.shapesize(0.9, 0.9, 0)
ball.setheading(initial_heading)


player1 = Turtle()
player1.shape("square")
player1.color("white")
player1.penup()
player1.setheading(90)
player1.shapesize(0.2, 3,0)
player1.goto(x=-450, y=0)

player2 = Turtle()
player2.shape("square")
player2.color("white")
player2.setheading(90)
player2.shapesize(0.2, 3,0)
player2.penup()
player2.goto(x=450, y=0)

screen.listen()
screen.onkey(key="w", fun=up_player1)
screen.onkey(key="s", fun=down_player1)
screen.onkey(key="Up", fun=up_player2)
screen.onkey(key="Down", fun=down_player2)

while is_game_on:
  screen.update()
  time.sleep(0.1)
  ball.forward(20)

  #ball hitting the wall
  if (ball.ycor() > 220.0) or (ball.ycor() < -220.0):
    if ball.heading() > 0.0 and ball.heading() < 90.0:
      ball.right(90)
    elif ball.heading() > 90.0 and ball.heading() < 180.0:
      ball.left(90)
    elif ball.heading() > 180.0 and ball.heading() < 270.0:
      ball.right(90)
      screen.update()
      time.sleep(0.1)
      ball.forward(20)
    else:
      ball.left(90)
      screen.update()
      time.sleep(0.1)
      ball.forward(20)

  if (ball.distance(player1) <= 20 or ball.distance(player2) <= 20):
    if round(ball.heading()) == 0 or round(ball.heading()) == 360:
      ball.left(180)
      screen.update()
      time.sleep(0.1)
      ball.forward(20)
    elif round(ball.heading()) == 180:
      ball.left(180)
      screen.update()
      time.sleep(0.1)
      ball.forward(20)
    if ball.heading() > 0.0 and ball.heading() < 90.0:
      ball.left(90)
      screen.update()
      time.sleep(0.1)
      ball.forward(20)
    elif ball.heading() > 90.0 and ball.heading() < 180.0:
      ball.right(90)
      screen.update()
      time.sleep(0.1)
      ball.forward(20)
    elif ball.heading() > 180.0 and ball.heading() < 270.0:
      ball.left(90)
      screen.update()
      time.sleep(0.1)
      ball.forward(20)
    else:
      ball.right(90)
      screen.update()
      time.sleep(0.1)
      ball.forward(20)


screen.exitonclick()