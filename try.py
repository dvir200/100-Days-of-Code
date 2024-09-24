from turtle import Turtle
import random

COLORS = ["blue", "black","white", "red", "yellow", "green", "purple", "pink"]
STEPS = 10

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.color(random.choice("blue"))
