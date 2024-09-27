import colorgram
from turtle import Turtle, Screen
import random 


colors = colorgram.extract('Day 18\Hirst Painting Project\image.jpg', 30)

rgb_from_extraction = []
for x in range (30):
  color = colors[x]
  rgb_from_extraction.append((color.rgb[0], color.rgb[1], color.rgb[2]))

painter = Turtle()
screen = Screen()
screen.colormode(255)
painter.hideturtle()


def paintLine(pos_x, pos_y, set_of_colors):
  painter.penup()
  for x in range (10):
    painter.goto(pos_x, pos_y)
    painter.pencolor(random.choice(set_of_colors))
    painter.dot(20)
    pos_x += 50

start_pos_x = -200
start_pos_y = -200

for x in range (10):
  paintLine(start_pos_x, start_pos_y, rgb_from_extraction)
  start_pos_y += 50

painter.hideturtle()

screen.exitonclick()