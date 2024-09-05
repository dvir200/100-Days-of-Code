from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Ariel', 20)

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(x=0, y=270)
    self.write("Score: 0", move=False, align=ALIGNMENT, font=FONT)

  def game_over(self):
    self.goto(x=0, y=0)
    self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)

  def increase_score(self):
    self.clear()
    self.score += 1
    self.write(f"Score: {self.score}", move=False, align="center", font=('Ariel', 20))