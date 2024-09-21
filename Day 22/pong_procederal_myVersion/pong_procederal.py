# required modules
from turtle import Turtle, Screen
import time
import random

# key mapping functions
def up_player1():
  player1.setheading(90)
  player1.forward(20)

def down_player1():
  player1.back(20)

def up_player2():
  player2.setheading(90)
  player2.forward(20)

def down_player2():
  player2.back(20)




# screen object initializing
screen = Screen()
screen.setup(width=1000, height=480)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)
screen.update()

# variable initializing
is_game_on = True
p1_score = 0
p2_score = 0
start_heading = [0.0, 20.0, 30.0, 160.0, 180.0, 190.0, 200.0, 330.0, 360.0]

# scoreboard for player 1 initializing
scoreboard_p1 = Turtle()
scoreboard_p1.hideturtle()
scoreboard_p1.penup()
scoreboard_p1.color("white")
scoreboard_p1.goto(x=-250, y=200)
scoreboard_p1.write(f"{p1_score}", move=False, align="center", font=('Ariel', 20))

# scoreboard for player 2 initializing
scoreboard_p2 = Turtle()
scoreboard_p2.hideturtle()
scoreboard_p2.penup()
scoreboard_p2.color("white")
scoreboard_p2.goto(x=250, y=200)
scoreboard_p2.write(f"{p2_score}", move=False, align="center", font=('Ariel', 20))

# ball initializing
ball = Turtle()
ball.penup()
ball.shape("circle")
ball.color("white")
ball.shapesize(0.9, 0.9, 0)
ball.setheading(random.choice(start_heading))
""" ball.speed("slowest") """


# player 1 initializing
player1 = Turtle()
player1.shape("square")
player1.color("white")
player1.penup()
player1.setheading(90)
player1.shapesize(0.2, 3,0)
player1.goto(x=-450, y=0)
player1.speed("fastest")

# player 2 initializing
player2 = Turtle()
player2.shape("square")
player2.color("white")
player2.setheading(90)
player2.shapesize(0.2, 3,0)
player2.penup()
player2.goto(x=450, y=0)
player2.speed("fastest")

# key listening
screen.listen()
screen.onkeypress(key="w", fun=up_player1)
screen.onkeypress(key="s", fun=down_player1)
screen.onkeypress(key="Up", fun=up_player2)
screen.onkeypress(key="Down", fun=down_player2)

# game logic
while is_game_on:
  screen.update()
  time.sleep(0.1)
  ball.forward(10)

  # ball hitting the wall
  if ball.ycor() > 215.0 or ball.ycor() < -215.0:
    ball.setheading(360 - ball.heading())
    """ while ball.ycor() > 215.0:
      screen.update()
      time.sleep(0.1)
      ball.forward(10) """
    

  # ball bounce off paddle     
  if ball.distance(player1) <= 20 or ball.distance(player2) <= 20:
    ball.setheading((ball.heading() + 180) % 360)
    while ball.distance(player1) <= 20 or ball.distance(player2) <= 20:
        screen.update()
        time.sleep(0.1)
        ball.forward(10)


  # ball passes one of the paddles
  if ball.xcor() > 490:
    scoreboard_p1.clear()
    p1_score += 1
    scoreboard_p1.write(f"{p1_score}", move=False, align="center", font=('Ariel', 20))
    ball.goto(x=0, y=0)
    ball.setheading(random.choice(start_heading))
  
  elif ball.xcor() < -490:
    scoreboard_p2.clear()
    p2_score += 1
    scoreboard_p2.write(f"{p2_score}", move=False, align="center", font=('Ariel', 20))
    ball.goto(x=0, y=0)
    ball.setheading(random.choice(start_heading))

screen.exitonclick()


