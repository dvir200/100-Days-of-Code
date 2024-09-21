from turtle import Turtle, Screen

PADDLE_WIDTH = 0.3
PADDLE_LENGTH = 3
PADDLE_OUTLINE = 0
PADDLE_UP_HEADING = 90
PADDLE_DOWN_HEADING = 270
PADDLE_COLOR = "white"
PADDLE_SHAPE = "square"
PADDLE_STEPS = 20

class paddle:
  def __init__(self):
    self = Turtle()
    self.hideturtle()
    self.penup()
    self.shape(PADDLE_SHAPE)
    self.color(PADDLE_COLOR)
    self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LENGTH, outline=PADDLE_OUTLINE)
    self.setheading(PADDLE_UP_HEADING)

  def paddle_up(self):
    self.forward(PADDLE_STEPS)

  def paddle_down(self):
    self.back(PADDLE_STEPS)

  def set_initial_coordinates(self, x_parameter, y_parameter):
    self.goto(x=x_parameter, y=y_parameter)
  