from turtle import Turtle
import random

COLORS = ["blue", "black","white", "red", "yellow", "green", "purple", "pink"]
STEPS = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(x=0, y=random.randint(0,280))
        self.setheading(180)

    def move(self):
        self.forward(STEPS)

