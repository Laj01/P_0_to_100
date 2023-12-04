from turtle import Turtle, Screen
import time

# Set up the starting screen
screen = Screen()
screen.setup(width=600, height=600)
screen.cv._rootwindow.resizable(False, False)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Snake')

# Add the starting snake body to the screen
start_positions = [(0, 0), (-20, 0), (-40, 0),]
parts = []
for position in start_positions:
    part = Turtle(shape='square')
    part.color('white')
    part.penup()
    part.goto(position)
    parts.append(part)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for part_num in range(len(parts) - 1, 0, -1):
        newx = parts[part_num - 1].xcor()
        newy = parts[part_num - 1].ycor()
        parts[part_num].goto(newx, newy)
    parts[0].forward(20)

screen.exitonclick()