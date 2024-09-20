from turtle import Turtle, Screen
import time
import random

def up_player1():
  player1.setheading(90)
  player1.forward(10)

def down_player1():
  player1.setheading(270)
  player1.forward(10)

def up_player2():
  player2.setheading(90)
  player2.forward(10)

def down_player2():
  player2.setheading(270)
  player2.forward(10)


screen = Screen()
screen.setup(width=1000, height=480)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

is_game_on = True
p1_score = 0
p2_score = 0
initial_heading = random.randrange(0, 360)
screen.update()

scoreboard_p1 = Turtle()
scoreboard_p1.hideturtle()
scoreboard_p1.penup()
scoreboard_p1.color("white")
scoreboard_p1.goto(x=-250, y=200)
scoreboard_p1.write(f"{p1_score}", move=False, align="center", font=('Ariel', 20))

scoreboard_p2 = Turtle()
scoreboard_p2.hideturtle()
scoreboard_p2.penup()
scoreboard_p2.color("white")
scoreboard_p2.goto(x=250, y=200)
scoreboard_p2.write(f"{p2_score}", move=False, align="center", font=('Ariel', 20))


ball = Turtle()
ball.penup()
ball.shape("circle")
ball.color("white")
ball.shapesize(0.9, 0.9, 0)
ball.setheading(initial_heading)
""" ball.speed("slowest") """



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

prev_iter_turn = False

while is_game_on:
  screen.update()
  time.sleep(0.1)
  ball.forward(10)

  if ball.ycor() < 220.0 or ball.ycor() > -220.0:
    prev_iter_turn = False

  #ball hitting the wall
  if prev_iter_turn is False:
    if ball.ycor() > 215.0:
        if ball.heading() > 0.0 and ball.heading() < 90.0:
          prev_iter_turn = True
          ball.right(90)
          while ball.ycor() > 215.0:
            screen.update()
            time.sleep(0.1)
            ball.forward(10)
        elif ball.heading() > 90.0 and ball.heading() < 180.0:
          prev_iter_turn = True
          ball.left(90)
          while ball.ycor() > 215.0:
            screen.update()
            time.sleep(0.1)
            ball.forward(10)
    elif ball.ycor() < -215.0:
      if ball.heading() > 180.0 and ball.heading() < 270.0:
        prev_iter_turn = True
        ball.right(90)
        while ball.ycor() <-215.0:
          screen.update()
          time.sleep(0.1)
          ball.forward(10)
      elif ball.heading() > 270.0 and ball.heading() < 360.0:
        prev_iter_turn = True
        ball.left(90)
        while ball.ycor() <-215.0:
          screen.update()
          time.sleep(0.1)
          ball.forward(10)
  else:
    pass
    

  #ball bounce off paddle     
  if ball.distance(player1) <= 20:
    if ball.towards(player1.pos()) < 180.0 and ball.towards(player1.pos()) > 140.0:
      ball.right(120)
      while ball.distance(player1) <= 20:
        screen.update()
        time.sleep(0.1)
        ball.forward(10)
    elif ball.towards(player1.pos()) > 180.0 and ball.towards(player1.pos()) < 210.0:
      ball.right(120)
      while ball.distance(player1) <= 20:
        screen.update()
        time.sleep(0.1)
        ball.forward(10)
    elif ball.towards(player1.pos()) == 180.0:
      ball.right(180)
      while ball.distance(player1) <= 20:
        screen.update()
        time.sleep(0.1)
        ball.forward(10)

  if ball.distance(player2) <= 20:
    if ball.towards(player2.pos()) > 0.0 and ball.towards(player2.pos()) < 30.0:
      ball.left(120)
      while ball.distance(player2) <= 20:
        screen.update()
        time.sleep(0.1)
        ball.forward(10)
    elif ball.towards(player2.pos()) < 360.0 and ball.towards(player2.pos()) < 330.0:
      ball.right(120)
      while ball.distance(player2) <= 20:
        screen.update()
        time.sleep(0.1)
        ball.forward(10)
    elif ball.towards(player2.pos()) == 0.0 or ball.towards(player2.pos()) == 360.0:
      ball.right(180)
      while ball.distance(player2) <= 20:
        screen.update()
        time.sleep(0.1)
        ball.forward(10)

  if ball.xcor() > 490:
    scoreboard_p1.clear()
    p1_score += 1
    scoreboard_p1.write(f"{p1_score}", move=False, align="center", font=('Ariel', 20))
    ball.goto(x=0, y=0)
    initial_heading = random.randrange(0, 360)
    ball.setheading(initial_heading)
  
  elif ball.xcor() < -490:
    scoreboard_p2.clear()
    p2_score += 1
    scoreboard_p2.write(f"{p2_score}", move=False, align="center", font=('Ariel', 20))
    ball.goto(x=0, y=0)
    initial_heading = random.randrange(0, 360)
    ball.setheading(initial_heading)

screen.exitonclick()


