from turtle import Turtle

class PlayerChar(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x=0, y=-280)
        self.setheading(90)

    def move_forward(self):
        self.setheading(90)
        self.forward(10)

    def move_right(self):
        self.setheading(0)
        self.forward(10)

    def move_left(self):
        self.setheading(180)
        self.forward(10)

    def move_backwards(self):
        self.setheading(270)
        self.forward(10)
