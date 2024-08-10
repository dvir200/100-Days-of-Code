from turtle import Turtle, Screen
import random 

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("azure4")

screen = Screen()



""" for x in range (3, 11):
  screen.colormode(255)
  degree = 360 / x
  R = randint(0, 255)
  G = randint(0, 255)
  B = randint(0, 255)
  timmy_the_turtle.color(R, G, B)
  for x in range (x):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(degree) """

""" directions = ["north", "east", "south", "west"]
while True:
  screen.colormode(255)
  R = random.randint(0, 255)
  G = random.randint(0, 255)
  B = random.randint(0, 255)
  timmy_the_turtle.color(R, G, B)

  timmy_the_turtle.pensize(10)

  choice = random.choice(directions)

  if choice is "north":
    timmy_the_turtle.setheading(90)
    timmy_the_turtle.forward(10)
  elif choice is "east":
    timmy_the_turtle.setheading(0)
    timmy_the_turtle.forward(50)
  elif choice is "south":
    timmy_the_turtle.setheading(180)
    timmy_the_turtle.forward(50)
  else:
    timmy_the_turtle.setheading(270)
    timmy_the_turtle.forward(50) """


""" timmy_the_turtle.circle(100)
timmy_the_turtle.setheading(180)
timmy_the_turtle.circle(100) """


screen.colormode(255)
for x in range (0, 360, 5):
  R = random.randint(0, 255)
  G = random.randint(0, 255)
  B = random.randint(0, 255)
  timmy_the_turtle.color(R, G, B)
  timmy_the_turtle.speed(100)
  timmy_the_turtle.circle(100)
  timmy_the_turtle.setheading(x)
  





screen.exitonclick()