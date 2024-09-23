from turtle import Turtle

SCOREBOARD_COLOR = "white"
SCOREBOARD_FONT = ('Ariel', 20)


class Scoreboard(Turtle):
  def __init__(self, x_parameter, y_parameter):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.color(SCOREBOARD_COLOR)
    self.player_score = 0
    self.goto(x=x_parameter, y=y_parameter)
    self.write(f"{self.player_score}", move=False, align="center", font=SCOREBOARD_FONT)


  def add_score(self):
    self.clear()
    self.player_score += 1
    self.write(f"{self.player_score}", move=False, align="center", font=SCOREBOARD_FONT)
