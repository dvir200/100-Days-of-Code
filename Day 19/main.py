from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width= 500, height=400)
user_bet = screen.textinput(title= "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
turtle_list = []

for turtle_instance in range (0,6):
  new_t = Turtle(shape= "turtle")
  new_t.penup()
  new_t.color(colors[turtle_instance])
  new_t.goto(x = -230, y = y_positions[turtle_instance])
  turtle_list.append(new_t)

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in turtle_list:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_turtle = turtle.pencolor()
      if winning_turtle == user_bet:
        print(f"You've Won! The {winning_turtle} turtle is the winner!")
      else:
        print(f"You've lost. The winning turtle is {winning_turtle}")
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)


screen.exitonclick()