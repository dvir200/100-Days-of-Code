from turtle import Turtle

class PlayerChar(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(x=0, y=-280)
        self.setheading(90)


    def move_forward(self):
        self.forward(10)

    def reset_pos(self):
        self.goto(x=0, y=-280)

