from turtle import Turtle, Screen
from try2 import  PlayerChar



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("grey")
screen.tracer(0)
screen.update()

car = Turtle()
car.shape("square")
car.shapesize(stretch_wid=1, stretch_len=2)
car.penup()
car.setheading(180)
car.color("blue")

player = PlayerChar()

screen.listen()
screen.onkey(fun=player.move_forward, key="Up")
screen.onkey(fun=player.move_right, key="Right")
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=player.move_backwards, key="Down")

while True:
    screen.update()

    print(f"distance to object: {player.distance(car)}")
    print()

screen.exitonclick()
