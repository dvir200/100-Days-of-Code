from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Initialization of game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialization of objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

# Key listening
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

# Game function with loop + boolean variable
game_is_on = True
while game_is_on:

  # Snake moving
  screen.update()
  time.sleep(0.1)
  snake.move()

  # Collision with food
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()
  
  # Boundries collision detection
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() > 280:
    game_is_on = False
    scoreboard.game_over()

  # Tail collision detection
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()

screen.exitonclick()