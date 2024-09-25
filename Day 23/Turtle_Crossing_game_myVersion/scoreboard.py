from turtle import Turtle

COLOR = "white"
LEVEL = 0
FONT = ('Ariel', 20)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor(COLOR)
        self.goto(x=-330, y=250)
        self.update()

    def update(self):
        self.clear()
        global LEVEL
        LEVEL += 1
        self.write(f"Level: {LEVEL}", move=False, align="center", font=FONT)

    def end_game(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align="center", font=FONT)
