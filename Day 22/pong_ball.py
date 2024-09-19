from turtle import Turtle
import random
import time

STEPS = 10
INITIAL_HEADING = random.randrange(0,360)

class Ball:
  def __init__(self):
    self.segment = []
    self.initiate_ball()
    self.head = self.segment[0]


  def initiate_ball(self):
    ball = Turtle()
    ball.penup()
    ball.shape("square")
    ball.color("white")
    ball.setheading(INITIAL_HEADING)
    self.segment.append(ball)

  def movement(self):
    self.head.forward(STEPS)
    time.sleep(0.3)
    """ if (self.head.ycor() == 200) or (self.head.ycor() == -200):
      self.change_direction() """

  def change_direction(self):
    if self.head.heading() > 0 and self.head.heading() < 90:
      self.head.right(60)
      return self.head
    elif self.head.heading() > 90 and self.head.heading() < 180:
      self.head.left(60)
      return self.head
    elif self.head.heading() > 180 and self.head.heading() < 270:
      self.head.right(60)
      return self.head
    else:
      self.head.left(60)
      return self.head


#goes in movement fuction
"""     rand_direction = random.randint(0, 360)
    self.head.setheading(rand_direction)

    while True:
      time.sleep(0.3)
      if (self.head.ycor() == 200) or (self.head.ycor() == -200):
        self.change_direction()
      
      self.head.forward(STEPS) """
  
