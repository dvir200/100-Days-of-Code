from turtle import Turtle

PADDLE_WIDTH = 0.3
PADDLE_LENGTH = 3
PADDLE_OUTLINE = 0
PADDLE_UP_HEADING = 90
PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"
PADDLE_STEPS = 20

class Paddle(Turtle):
  def __init__(self, x_parameter, y_parameter):
    super().__init__()
    self.penup()
    self.shape(PADDLE_SHAPE)
    self.color(PADDLE_COLOR)
    self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH, outline=PADDLE_OUTLINE)
    self.setheading(PADDLE_UP_HEADING)
    self.goto(x=x_parameter, y=y_parameter)
    self.speed("fastest")

  def paddle_up(self):
    self.forward(PADDLE_STEPS)

  def paddle_down(self):
    self.back(PADDLE_STEPS)

  def set_coordinates(self, x_parameter, y_parameter):
    self.goto(x=x_parameter, y=y_parameter)
  