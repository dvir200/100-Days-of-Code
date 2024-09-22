from ball import Ball
from scoreboard import Scoreboard
from paddle import Paddle
from turtle import Screen

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 480
SCREEN_COLOR = "black"
SCREEN_TITLE = "Pong Game"

PLAYER_1_UP_KEY = "w"
PLAYER_1_DOWN_KEY = "s"
PLAYER_2_UP_KEY = "Up"
PLAYER_2_DOWN_KEY = "Down"

SCOREBOARD_P1_X_VALUE = -250
SCOREBOARD_P2_X_VALUE = 250
SCOREBOARD_Y_VALUE = 200

PADDLE_P1_X_VALUE = -450
PADDLE_P2_X_VALUE = 450
PADDLE_Y_VALUE = 0

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title(SCREEN_TITLE)
screen.bgcolor(SCREEN_COLOR)
screen.tracer(0)
screen.update()

is_game_on = True

scoreboard_p1 = Scoreboard(x_parameter = SCOREBOARD_P1_X_VALUE, y_parameter = SCOREBOARD_Y_VALUE)
scoreboard_p2 = Scoreboard(x_parameter = SCOREBOARD_P2_X_VALUE, y_parameter = SCOREBOARD_Y_VALUE)

ball = Ball()

player1 = Paddle(x_parameter=PADDLE_P1_X_VALUE, y_parameter=PADDLE_Y_VALUE)

player2 = Paddle(x_parameter=PADDLE_P2_X_VALUE, y_parameter=PADDLE_Y_VALUE)

screen.listen()
screen.onkeypress(key=PLAYER_1_UP_KEY, fun=player1.paddle_up())
screen.onkeypress(key=PLAYER_1_DOWN_KEY, fun=player1.paddle_down())
screen.onkeypress(key=PLAYER_2_UP_KEY, fun=player2.paddle_up())
screen.onkeypress(key=PLAYER_2_DOWN_KEY, fun=player2.paddle_down())

while is_game_on:
  ball.move(screen_obj=screen)

  ball.wall_bounce()

  if ball.distance(player1) <= 20 or ball.distance(player2) <= 20:
    ball.paddle_bounce()
    while ball.distance(player1) <= 20 or ball.distance(player2) <= 20:
      ball.move(screen_obj=screen)

  if ball.xcor() > 490:
    scoreboard_p1.add_score()
    ball.fresh_start()
  
  elif ball.xcor() < -490:
    scoreboard_p2.add_score()
    ball.fresh_start()

screen.exitonclick()