from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
screen.update()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  if snake.head.distance(food) < 15:
    food.refresh()
  
  

screen.exitonclick()