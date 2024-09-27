from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Ariel', 20)

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    with open("Day 20 + 21\data.txt", mode="r") as file:
      self.high_score = int(file.read())
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(x=0, y=270)
    self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

  def update_scoreboard(self):
    self.clear()
    with open("Day 20 + 21\data.txt", mode="r") as file:
      temp = int(file.read())
      if temp > self.high_score:
        self.high_score = temp
    self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=('Ariel', 20))

  def reset(self):
    if self.score > self.high_score:
      with open("Day 20 + 21\data.txt", mode="w") as file:
        file.write(str(self.score))
    self.score = 0
    self.update_scoreboard()


  def increase_score(self):
    self.score += 1
    self.update_scoreboard
    