from turtle import Turtle
from random import choice
from time import sleep

BALL_WIDTH = 0.9
BALL_LENGTH = 0.9
BALL_OUTLINE = 0
BALL_STARTING_POS = [0.0, 20.0, 30.0, 160.0, 180.0, 190.0, 200.0, 330.0, 360.0]
BALL_SHAPE = "circle"
BALL_COLOR = "white"
BALL_STEPS = 10

SLEEP_VALUE = 0.1

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self = Turtle()
    self.penup()
    self.shape("circle")
    self.shapesize(stretch_wid=BALL_WIDTH, stretch_len=BALL_LENGTH, outline=BALL_OUTLINE)
    self.color("white")

  def choose_start_heading(self):
    self.setheading(choice(BALL_STARTING_POS))
  

  def wall_bounce(self):
    if self.ycor() > 215.0 or self.ycor() < -215.0:
      self.setheading(360 - self.heading())
    
  def paddle_bounce(self):
    self.setheading((self.heading() + 180) % 360)

  def fresh_start(self):
    self.goto(x=0, y=0)
    self.choose_start_heading()

  def move(self, screen_obj):
    screen_obj.update()
    sleep(SLEEP_VALUE)
    self.forward(BALL_STEPS)


